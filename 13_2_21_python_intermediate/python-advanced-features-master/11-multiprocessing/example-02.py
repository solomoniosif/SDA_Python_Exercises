import logging
import time
import multiprocessing
import math

l = logging.getLogger("multiprocessing")
h = logging.StreamHandler()
f = logging.Formatter("%(asctime)s: %(message)s")
h.setFormatter(f)
l.addHandler(h)
l.setLevel(logging.INFO)


def square_root(num):
    for _ in range(10_000_000):
        result = math.sqrt(num)
    l.info(f"sqrt of {num} is {result:.1f}")


if __name__ == "__main__":
    big_float = 123_456_789
    processes = [
        multiprocessing.Process(target=square_root, args=(big_float,)) for i in range(5)
    ]
    start_time = time.time()
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    delta_time = time.time() - start_time
    print(f"It took {delta_time:.1f}s to calculate square roots.")
