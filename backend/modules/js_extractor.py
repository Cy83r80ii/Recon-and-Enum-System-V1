import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def extract_js_endpoints(url):

    endpoints = []

    try:

        r = requests.get(url, timeout=5)

        soup = BeautifulSoup(r.text, "html.parser")

        scripts = soup.find_all("script", src=True)

        for script in scripts:

            js_url = urljoin(url, script["src"])

            try:

                js = requests.get(js_url, timeout=5).text

                matches = re.findall(r"/api/[a-zA-Z0-9/_-]+", js)

                endpoints.extend(matches)

            except:
                pass

    except:
        pass

    return endpoints
