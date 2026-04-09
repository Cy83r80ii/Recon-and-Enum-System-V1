import urllib.parse


def extract_params(urls):

    params = []

    for url in urls:

        parsed = urllib.parse.urlparse(url)

        if parsed.query:

            query = urllib.parse.parse_qs(parsed.query)

            for param in query:

                params.append({
                    "url": url,
                    "param": param
                })

    return params
