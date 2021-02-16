import requests
import time
import logging
import multiprocessing

l = logging.getLogger()
h = logging.StreamHandler()
f = logging.Formatter("%(asctime)s: %(message)s")
h.setFormatter(f)
l.addHandler(h)
l.setLevel(logging.INFO)


def request_process(pipe):
    url = pipe.recv()
    while url is not None:
        start_time = time.time()
        requests.get(url)
        l.info(f"{url} took {time.time() - start_time:.1f}s")
        url = pipe.recv()


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
    urls_parent, urls_child = multiprocessing.Pipe()
    proc = multiprocessing.Process(target=request_process, args=(urls_child,))
    proc.start()
    for url in urls:
        urls_parent.send(url)
    urls_parent.send(None)
    proc.join()
