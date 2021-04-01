###############################
# TODO: Stack implementation
###############################

class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, x):
        self.__stack.append(x)

    def pop(self):
        self.__stack.pop()

    def __len__(self):
        return len(self.__stack)

    def is_empty(self):
        return len(self.__stack) == 0
