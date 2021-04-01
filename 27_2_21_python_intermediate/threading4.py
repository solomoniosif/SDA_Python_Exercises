import timeit


def count(_from, _to):
    while _from >= _to:
        _from -= 1


def wo_threading_func():
    count(400000, 0)


def with_threading_func():
    import threading

    t1 = threading.Thread(target=count, args=(400000, 200000))
    t2 = threading.Thread(target=count, args=(200000, 0))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


def with_multiprocessing_func():
    import multiprocessing

    p1 = multiprocessing.Process(target=count, args=(400000, 200000))
    p2 = multiprocessing.Process(target=count, args=(200000, 0))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == "__main__":
    wo_threading = "wo_threading_func()"
    with_threading = "with_threading_func()"
    with_multiprocessing = "with_multiprocessing_func()"
    setup = "from __main__ import wo_threading_func, with_threading_func, with_multiprocessing_func"

    print("Without threads:", timeit.timeit(stmt=wo_threading,
                                            setup=setup,
                                            number=100))
    print("With threads:", timeit.timeit(stmt=with_threading,
                                         setup=setup,
                                         number=100))
    print("With sub-processes:", timeit.timeit(stmt=with_multiprocessing,
                                               setup=setup,
                                               number=100))
