import asyncio
import time

from modules.crawler import crawl
from modules.param_extractor import extract_params
from modules.js_extractor import extract_js_endpoints

from modules.xss import scan_xss
from modules.sqli import scan_sqli
from modules.idor import scan_idor
from modules.path_traversal import scan_path_traversal
from modules.wordpress import scan_wordpress
from modules.dom_xss import scan_dom_xss

from modules.dir_bruteforce import scan_directories
from modules.subdomain import scan_subdomains

from modules.api_fuzzer import scan_api
from modules.param_fuzzer import fuzz_params
from modules.api_detector import detect_api
from modules.waf_detector import detect_waf

from integrations.nuclei_runner import run_nuclei

from utils.dedupe import remove_duplicates
from utils.pdf_report import generate_report

from state import scan_state


# -----------------------------
# LOG FUNCTION
# -----------------------------
def log(message):
    print("[ENGINE]", message)
    scan_state["logs"].append(message)


# -----------------------------
# MAIN SCAN FUNCTION
# -----------------------------
def run_scan(target, mode="quick"):

    start = time.time()
    findings = []

    # Reset state
    scan_state["logs"] = []
    scan_state["progress"] = 0

    log("================================")
    log(f"Target: {target}")
    log(f"Mode: {mode}")
    log("================================")

    # -----------------------------
    # Mode config
    # -----------------------------
    if mode == "quick":
        max_urls, depth, param_limit = 50, 1, 20
    elif mode == "deep":
        max_urls, depth, param_limit = 150, 2, 50
    elif mode == "aggressive":
        max_urls, depth, param_limit = 300, 3, 100
    else:
        max_urls, depth, param_limit = 50, 1, 20

    # -----------------------------
    # WAF Detection
    # -----------------------------
    try:
        waf = detect_waf(target)
        if waf:
            findings.extend(waf)
        log("WAF detection finished")
    except Exception as e:
        log(f"WAF ERROR: {e}")

    scan_state["progress"] = 10

    # -----------------------------
    # Crawling
    # -----------------------------
    try:
        urls = crawl(target, max_urls=max_urls, depth=depth)
    except Exception as e:
        log(f"Crawler ERROR: {e}")
        urls = []

    urls = remove_duplicates(urls)

    log(f"URLs discovered: {len(urls)}")

    if not urls:
        log("WARNING: No URLs found")

    scan_state["progress"] = 20

    # -----------------------------
    # JS Extraction
    # -----------------------------
    js_endpoints = []

    for url in urls[:20]:
        try:
            js = extract_js_endpoints(url)
            if js:
                js_endpoints.extend(js)
        except Exception as e:
            log(f"JS ERROR ({url}): {e}")

    urls.extend(js_endpoints)
    urls = remove_duplicates(urls)

    log(f"JS endpoints discovered: {len(js_endpoints)}")

    scan_state["progress"] = 30

    # -----------------------------
    # Param Extraction
    # -----------------------------
    try:
        params = extract_params(urls)
    except Exception as e:
        log(f"Param ERROR: {e}")
        params = []

    params = remove_duplicates(params)

    log(f"Parameters to test: {len(params)}")

    if not params:
        log("WARNING: No parameters found")

    scan_state["progress"] = 40

    # -----------------------------
    # DOM XSS
    # -----------------------------
    try:
        dom = scan_dom_xss(urls)
        if dom:
            findings.extend(dom)
        log("DOM XSS finished")
    except Exception as e:
        log(f"DOM XSS ERROR: {e}")

    scan_state["progress"] = 50

    # -----------------------------
    # Async scans
    # -----------------------------
    async def run_async():
        try:
            tasks = [
                scan_xss(params),
                scan_sqli(params)
            ]

            results = await asyncio.gather(*tasks, return_exceptions=True)

            merged = []
            for r in results:
                if isinstance(r, list):
                    merged.extend(r)
                else:
                    log(f"Async ERROR: {r}")

            return merged

        except Exception as e:
            log(f"Async Scan ERROR: {e}")
            return []

    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        async_results = loop.run_until_complete(run_async())
        findings.extend(async_results)

        log("Async vulnerability scans finished")

    except Exception as e:
        log(f"Async Execution ERROR: {e}")

    scan_state["progress"] = 65

    # -----------------------------
    # Additional Modules
    # -----------------------------
    def safe_run(name, func, *args):
        try:
            result = func(*args)
            if result:
                findings.extend(result)
            log(f"{name} finished")
        except Exception as e:
            log(f"{name} ERROR: {e}")

    safe_run("IDOR", scan_idor, params)
    safe_run("Path Traversal", scan_path_traversal, params)
    safe_run("WordPress", scan_wordpress, target)

    scan_state["progress"] = 75

    safe_run("Nuclei", run_nuclei, target)

    scan_state["progress"] = 85

    # -----------------------------
    # Recon
    # -----------------------------
    safe_run("Directory Bruteforce", scan_directories, target)
    safe_run("Subdomain Scan", scan_subdomains, target)
    safe_run("API Fuzzing", scan_api, target)
    safe_run("Param Fuzzing", fuzz_params, urls[:param_limit])
    safe_run("API Detection", detect_api, target)

    scan_state["progress"] = 95

    # -----------------------------
    # Report
    # -----------------------------
    try:
        generate_report(findings, target)
        log("PDF report generated")
    except Exception as e:
        log(f"Report ERROR: {e}")

    # -----------------------------
    # Final
    # -----------------------------
    duration = round(time.time() - start, 2)

    log("================================")
    log(f"Findings: {len(findings)}")
    log(f"Duration: {duration}s")
    log("================================")

    scan_state["progress"] = 100

    return findings