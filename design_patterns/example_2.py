import time


class timer_decorator:
    def __init__(this, func):
        this.times = []
        this.func = func

    def __call__(this, *args, **kwargs):
        startTime = time.time()
        result = this.func(*args, **kwargs)
        deltaTime = time.time() - startTime
        this.times.append(deltaTime)
        print(
            f"Function {this.func.__name__} has been executed in {deltaTime}s with the following arguments: {args} {kwargs}"
        )
        return result


@timer_decorator
def calculateProductAMillion_times(small_number):
    for _ in range(1_000_000):
        LARGE_NUMBER = 4 ** 39
        _ = LARGE_NUMBER * small_number + small_number ** 39


if __name__ == """__main__""":
    calculateProductAMillion_times(10)
