from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import asyncio

from engine import run_scan
from state import scan_state
app = FastAPI()

# ---------------------------------
# CORS
# ---------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------
# GLOBAL SCAN STATE
# ---------------------------------

scan_running = False

# ---------------------------------
# HELPER → ADD LOG
# ---------------------------------

def add_log(message):
    print("[ENGINE]", message)
    scan_state["logs"].append(message)


# ---------------------------------
# START SCAN
# ---------------------------------

@app.post("/scan")
async def start_scan(data: dict):

    global scan_running

    if scan_running:
        return {"status": "scan already running"}

    target = data.get("target")
    mode = data.get("mode", "quick")

    if not target:
        return {"error": "target required"}

    scan_running = True

    scan_state["target"] = target
    scan_state["status"] = "running"
    scan_state["progress"] = 0
    scan_state["findings"] = []
    scan_state["logs"] = []

    add_log(f"Target: {target}")
    add_log(f"Mode: {mode}")
    add_log("Initializing scan engine")

    loop = asyncio.get_event_loop()

    findings = await loop.run_in_executor(
        None,
        run_scan,
        target,
        mode
    )

    scan_state["findings"] = findings
    scan_state["status"] = "completed"
    scan_state["progress"] = 100

    add_log(f"Scan finished")
    add_log(f"Findings discovered: {len(findings)}")

    scan_running = False

    return {
        "status": "completed",
        "total_findings": len(findings)
    }

@app.get("/")
def home():
    return {"message": "Backend is running"}

# ---------------------------------
# RESULTS
# ---------------------------------

@app.get("/results")
def get_results():

    return {
        "status": scan_state["status"],
        "target": scan_state["target"],
        "findings": scan_state["findings"]
    }


# ---------------------------------
# PROGRESS
# ---------------------------------

@app.get("/progress")
def get_progress():

    return {
        "progress": scan_state["progress"]
    }


# ---------------------------------
# LOGS (for web terminal)
# ---------------------------------

@app.get("/logs")
def get_logs():

    return {
        "logs": scan_state["logs"][-50:]  # last 50 messages
    }


# ---------------------------------
# ROOT
# ---------------------------------

@app.get("/")
def home():

    return {
        "service": "ARES-X Backend",
        "status": "running"
    }