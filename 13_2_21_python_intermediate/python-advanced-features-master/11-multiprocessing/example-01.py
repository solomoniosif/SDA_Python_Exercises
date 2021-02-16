import logging
import time
import multiprocessing

l = logging.getLogger("multiprocessing")
h = logging.StreamHandler()
f = logging.Formatter("%(asctime)s: %(message)s")
h.setFormatter(f)
l.addHandler(h)
l.setLevel(logging.INFO)


def say_hello(i):
    l.info(f"Hello from #{i}")
    time.sleep(1)


if __name__ == "__main__":
    processes = [
        multiprocessing.Process(target=say_hello, args=(i + 1,)) for i in range(5)
    ]
    start_time = time.time()
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    delta_time = time.time() - start_time
    print(f"It took {delta_time:.1f}s to say hello.")
