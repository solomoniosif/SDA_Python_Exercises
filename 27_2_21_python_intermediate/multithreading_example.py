import threading
import time
import random


def iterate_print(iter):
    # A functions prints the elements of a list
    for item in iter:
        time.sleep(0.1)
        print(item)


if __name__ == "__main__":
    l1 = [n for n in range(5)]
    l2 = 'abcdefgh'

    t1 = threading.Thread(target=iterate_print, args=(l1,))

    t2 = threading.Thread(target=iterate_print, args=(l2,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print('Done!')
