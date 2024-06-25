import sys


class MinStack(object):

    def __init__(self):
        self.stack = []
        self.len_ = 0
        self.min = sys.maxsize

    def push(self, val):
        self.len_ += 1
        self.min = min(self.min, val)
        self.stack.append(val)

    def pop(self):
        self.len_ -= 1
        if self.len_ > 0:
            self.min = min(self.stack[:self.len_])
        else:
            self.min = sys.maxsize
        return self.stack.pop()

    def top(self):
        return self.stack[self.len_]

    def getMin(self):
        return self.min


if __name__ == "__main__":
    print(MinStack())