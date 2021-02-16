import time

class Timer:
    def __init__(self, func):
        self.func = func
        self.elapsed_time = 0

    def __call__(self, *args, **kwargs):
        print("Starting calculation ...")
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        self.elapsed_time = end_time - start_time
        # print(self.elapsed_time)
        return result


@Timer
def power(x, y):
    for _ in range(10_000_000):
        x ** y


if __name__ =="__main__":
    power(17, 15)
    print(power.elapsed_time)