import timeit
import requests


def crawl(url, dest):
    try:
        result = requests.get(url).text
        with open(dest, "a") as f:
            f.write(result)

    except requests.exceptions.RequestException:
        print("Error with URL check!")


def wo_threading_func(urls):
    for url in urls:
        crawl(url, "without_threads.txt")


def with_threading_func(urls):
    import threading

    threads = []
    for url in urls:
        th = threading.Thread(target=crawl, args=(url, "with_threads.txt"))
        th.start()
        threads.append(th)

    for th in threads:
        th.join()


if __name__ == "__main__":
    wo_threading = "wo_threading_func(urls)"
    with_threading = "with_threading_func(urls)"

    setup = '''
from __main__ import wo_threading_func, with_threading_func

urls = [
        "https://jsonplaceholder.typicode.com/comments/1",
        "https://jsonplaceholder.typicode.com/comments/2",
        "https://jsonplaceholder.typicode.com/comments/3"
    ]
        '''

    print("Without threads:", timeit.timeit(stmt=wo_threading,
                                            setup=setup,
                                            number=30))
    print("With threads:", timeit.timeit(stmt=with_threading,
                                         setup=setup,
                                         number=30))
