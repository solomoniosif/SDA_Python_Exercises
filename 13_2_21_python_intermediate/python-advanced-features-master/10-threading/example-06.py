import logging
import time
import concurrent.futures
import queue
import random

l = logging.getLogger("bakery")
h = logging.StreamHandler()
f = logging.Formatter("%(asctime)s: %(message)s")
h.setFormatter(f)
l.addHandler(h)
l.setLevel(logging.INFO)


class Bakery:
    def __init__(self):
        self.storage = queue.Queue()

    def baker(self):
        for i in range(12):
            self.storage.put(f"Bread #{i}")
            l.info("Finished baking")
            time.sleep(0.2)

    def customer(self, i):
        for _ in range(3):
            bread = self.storage.get()
            l.info(f"Customer #{i} got {bread}")
            time.sleep(random.uniform(0.5, 2.0))  # notice the random frequency


if __name__ == "__main__":
    mine = Bakery()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.submit(mine.baker)
        executor.submit(mine.customer, 1)
        executor.submit(mine.customer, 2)
        executor.submit(mine.customer, 3)
        executor.submit(mine.customer, 4)
