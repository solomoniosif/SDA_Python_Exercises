# Implementation of a custom iterator
class ZeroToN:
    def __init__(self, n):
        self.n = n

    def __iter__(self):  # called when iterator is created
        self.i = -1
        return self

    def __next__(self):  # called on next
        self.i += 1
        if self.i < self.n:
            return self.i
        else:
            raise StopIteration


for i in ZeroToN(10):
    print(i)
