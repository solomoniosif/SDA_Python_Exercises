import requests
import time
import logging
import concurrent.futures

l = logging.getLogger()
h = logging.StreamHandler()
f = logging.Formatter("%(asctime)s: %(message)s")
h.setFormatter(f)
l.addHandler(h)
l.setLevel(logging.INFO)


def req(url):
    l.info(f"Getting {url}...")
    return requests.get(url)


if __name__ == "__main__":
    urls = [
        "https://google.com",
        "https://amazon.com",
        "https://ebay.com",
        "https://bbc.co.uk",
        "https://youtube.com",
        "https://wikipedia.org",
        "https://twitter.com",
        "https://spotify.com",
        "https://uber.com",
        "https://apple.com",
        "https://microsoft.com",
    ]

    start = time.time()
    with concurrent.futures.ThreadPoolExecutor(len(urls)) as executor:
        results = executor.map(req, urls)
    l.info(f"Threading implementation took {time.time() - start:.2f}s")
