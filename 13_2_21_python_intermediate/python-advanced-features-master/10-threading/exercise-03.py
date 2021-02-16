"""
Write a class `Bakery`, which:
    - has a common variable called `storage` (int)
    - has a function called `baker()` which (for 10 loops) notes down current 
      state of the storage, sleeps for 0.1s and adds 1 to the storage, then 
      sleeps for 1s
    - has a function called `customer()` which (for 10 loops)notes down current 
      state of the storage, sleeps for 0.2s and removes 2 from the storage `if 
      storage >= 2`,, then sleeps for 1s
- use `threading.Lock` to prevent race conditions
- Run 2 customer threads and 1 baker thread
- Use logging to ensure all functions are working
"""
import logging
import time
import concurrent.futures
import threading

l = logging.getLogger("bakery")
h = logging.StreamHandler()
f = logging.Formatter("%(asctime)s: %(message)s")
h.setFormatter(f)
l.addHandler(h)
l.setLevel(logging.INFO)


class Bakery:
    def __init__(self):
        self.storage = 0
        self.__lock = threading.Lock()

    def baker(self):
        for _ in range(10):
            l.info("Baking bread...")
            with self.__lock:
                s = self.storage
                time.sleep(0.1)
                self.storage = s + 1
            l.info("Finished baking")
            time.sleep(1)

    def customer(self):
        for _ in range(10):
            with self.__lock:
                s = self.storage
                if s >= 2:
                    time.sleep(0.1)
                    self.storage = s - 2
                    l.info("Bought bread(2)")
            time.sleep(1)


if __name__ == "__main__":
    mine = Bakery()
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.submit(mine.customer)
        executor.submit(mine.baker)
        executor.submit(mine.customer)
