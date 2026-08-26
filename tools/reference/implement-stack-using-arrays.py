class ArrayStack:
    def __init__(self, capacity):
        self.items = [0] * capacity
        self.count = 0

    def push(self, x):
        if self.count < len(self.items):
            self.items[self.count] = x
            self.count += 1

    def pop(self):
        if self.count == 0:
            return -1
        self.count -= 1
        return self.items[self.count]

    def top(self):
        return self.items[self.count - 1] if self.count else -1

    def size(self):
        return self.count
