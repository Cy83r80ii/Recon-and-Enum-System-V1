import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36"
}

def crawl(start_url, max_urls=50, depth=1):
    visited = set()
    to_visit = [(start_url, 0)]
    found_urls = []

    while to_visit and len(found_urls) < max_urls:
        url, level = to_visit.pop(0)

        if url in visited or level > depth:
            continue

        visited.add(url)

        try:
            res = requests.get(url, headers=HEADERS, timeout=10)

            if res.status_code != 200:
                continue

            soup = BeautifulSoup(res.text, "lxml")

            for link in soup.find_all("a", href=True):
                new_url = urljoin(url, link["href"])

                # stay in same domain
                if urlparse(new_url).netloc == urlparse(start_url).netloc:
                    if new_url not in visited:
                        found_urls.append(new_url)
                        to_visit.append((new_url, level + 1))

        except Exception as e:
            print("[CRAWLER ERROR]", e)
            continue

    return found_urls