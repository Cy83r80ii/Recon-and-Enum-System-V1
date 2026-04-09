import re
from utils.http import session, TIMEOUT

patterns = [
r"[?&]([a-zA-Z0-9_]+)=",
r"([a-zA-Z0-9_]+):",
r"([a-zA-Z0-9_]+)\s*="
]

MAX_JS_PARAMS = 30


def extract_js_parameters(js_files):

    params = set()

    for js in js_files:

        try:

            r = session.get(js, timeout=TIMEOUT)

            for p in patterns:

                matches = re.findall(p, r.text)

                for m in matches:

                    if len(m) > 2:
                        params.add(m)

        except:
            pass

    return list(params)[:MAX_JS_PARAMS]
