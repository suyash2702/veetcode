class ArrayQueue:
    def __init__(self, capacity):
        self.items = [0] * capacity
        self.head = 0
        self.count = 0

    def push(self, x):
        if self.count < len(self.items):
            self.items[(self.head + self.count) % len(self.items)] = x
            self.count += 1

    def pop(self):
        if self.count == 0:
            return -1
        value = self.items[self.head]
        self.head = (self.head + 1) % len(self.items)
        self.count -= 1
        return value

    def front(self):
        return self.items[self.head] if self.count else -1

    def size(self):
        return self.count
