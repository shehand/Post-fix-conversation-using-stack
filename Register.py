class Register:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def isEmpty(self):
        return self.items == []

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
