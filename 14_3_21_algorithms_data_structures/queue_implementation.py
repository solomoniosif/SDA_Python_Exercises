
#######################################################
# TODO: Queue implementation based on a list (array)
#######################################################

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0)

    def front(self):
        return self.queue[0]

    def __str__(self):
        return str(self.queue)

    def __len__(self):
        return len(self.queue)


q = Queue()

print(f"Coada tocmai creata:  -> {q}")

for year in range(2010, 2020):
    q.enqueue(year)

print(q)

print(q.dequeue())
print(q.dequeue())

print(q)

print(q.front())