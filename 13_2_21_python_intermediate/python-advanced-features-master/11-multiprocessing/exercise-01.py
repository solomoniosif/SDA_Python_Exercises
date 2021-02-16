"""
1. Create the following functions:
    1. `generate_random(out_q, n)` which generates `n` random integers and puts them in `out_q` Queue
    2. `square(in_q, out_q, n)` which takes numbers from the `in_q` Queue and puts their squares in the `out_q`. 
    3. `to_binary(in_q, out_q, n)` takes numbers from the `in_q` Queue and puts their binary representations in the `out_q`. 
2. Create the three queues needed to connect functions in the following order:
    1. `generate_random`
    2. `queue_a`
    3. `square`
    4. `queue_b`
    5. `to_binary`
    6. `result_q`
3. Run the three functions in separate processes. Make `generate_random` generate 1000 integers.
4. Read all the items from `result_q` before calling `.join()`
5. You can add `timeout=<seconds>` to put/get calls to avoid deadlocks.
"""
import logging
import multiprocessing
import random


def generate_random(out_q, n):
    for _ in range(n):
        out_q.put(random.randint(1, 9999), timeout=2)


def square(in_q, out_q, n):
    for _ in range(n):
        num = in_q.get(timeout=2)
        out_q.put(num * num, timeout=2)


def to_binary(in_q, out_q, n):
    for _ in range(n):
        num = in_q.get(timeout=2)
        out_q.put(bin(num), timeout=2)


if __name__ == "__main__":
    queue_a = multiprocessing.Queue(maxsize=1001)
    queue_b = multiprocessing.Queue(maxsize=1001)
    result_q = multiprocessing.Queue(maxsize=1001)

    pipeline = [
        multiprocessing.Process(target=generate_random, args=(queue_a, 1000)),
        multiprocessing.Process(target=square, args=(queue_a, queue_b, 1000)),
        multiprocessing.Process(target=to_binary, args=(queue_b, result_q, 1000)),
    ]

    for p in pipeline:
        p.start()
    items = []
    for _ in range(1000):
        items.append(result_q.get(timeout=2))
    for p in pipeline:
        p.join()
    print(len(items))
