import re
from utils.http import session, TIMEOUT


patterns = [
r'["\'](/api/[^"\']+)["\']',
r'["\'](/v1/[^"\']+)["\']',
r'["\'](/graphql[^"\']*)["\']',
r'["\'](/admin[^"\']*)["\']'
]


def extract_js_endpoints(js_files):

    endpoints = set()

    for js in js_files:

        try:

            r = session.get(js, timeout=TIMEOUT)

            for p in patterns:

                matches = re.findall(p, r.text)

                for m in matches:
                    endpoints.add(m)

        except:
            pass

    return list(endpoints)
