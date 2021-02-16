import logging
import time
import concurrent.futures

l = logging.getLogger("toll_booth")
h = logging.StreamHandler()
f = logging.Formatter("%(asctime)s: %(message)s")
h.setFormatter(f)
l.addHandler(h)
l.setLevel(logging.INFO)


class TollBooth:
    def __init__(self):
        self.register = 0.0

    def process_fee(self, car, fee):
        l.info(f"Processing {car}'s fee. Current total: {self.register}")
        new_total = self.register + fee  # Toll booth calculates a new total
        time.sleep(0.1)  # processing takes 0.1 seconds
        self.register = new_total  # New total is saved after 0.1 seconds
        l.info(f"Done processing {car}'s fee. New total: {self.register}")


if __name__ == "__main__":
    cars = ["Red", "Blue", "Green"]
    booth = TollBooth()

    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        for c in cars:
            executor.submit(booth.process_fee, c, 10.0)
    delta_time = time.time() - start_time
    print(f"It took {delta_time:.1f}s to process all the cars.")
    print(f"Total: {booth.register}")
