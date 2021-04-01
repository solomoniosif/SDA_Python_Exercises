class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def empty(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)


sample_stack = Stack()
print(sample_stack)

for year in range(2012, 2021):
    sample_stack.push(year)

print(sample_stack)

print(sample_stack.pop())
print(sample_stack.pop())

print(sample_stack)

print(sample_stack.peek())
print(sample_stack)

sample_stack.empty()
print(sample_stack)
