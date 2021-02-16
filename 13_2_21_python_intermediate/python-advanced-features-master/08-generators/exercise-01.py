"""
Using example-03.py as reference, implement iterator `MyRange` which behaves just like built-in `range(start, stop, step)`
"""


class MyRange:
    def __init__(self, start, stop, step):
        self.position = start
        self.stop = stop
        self.step = step

    def __iter__(self):  # called when iterator is created
        self.position -= self.step
        return self

    def __next__(self):  # called on next
        self.position += self.step
        if self.position < self.stop:
            return self.position
        else:
            raise StopIteration


for i in MyRange(1, 7, 2):
    print(i)
