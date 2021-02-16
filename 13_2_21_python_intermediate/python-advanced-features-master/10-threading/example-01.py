import logging
import time

l = logging.getLogger("toll_booth")
h = logging.StreamHandler()
f = logging.Formatter("%(asctime)s: %(message)s")
h.setFormatter(f)
l.addHandler(h)
l.setLevel(logging.INFO)


def process_toll_booth_fee(car):
    l.info(f"Processing {car}'s fee...")
    time.sleep(2)  # processing takes 2 seconds
    l.info(f"Done processing {car}'s fee.")


if __name__ == "__main__":
    cars = ["Red", "Blue", "Green"]

    start_time = time.time()
    for car in cars:
        process_toll_booth_fee(car)
    delta_time = time.time() - start_time
    print(f"It took {delta_time:.1f}s to process all the cars.")
