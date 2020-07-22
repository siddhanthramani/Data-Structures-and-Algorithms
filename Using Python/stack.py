
# we implement stack using lists
# it can be implemented using linked lists and other methods also


class Stack:
    def __init__(self):
        self.items = []

    def pop(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to pop an empty stack.")

        topIdx = len(self.items) - 1
        item = self.items[topIdx]
        del self.items[topIdx]
        return item

    def push(self, item):
        self.items.append(item)

    def top(self):
        if self.isEmpty():
            raise RuntimeError(
                "Attempt to get the top element of an empty stack")

        return self.items[len(self.items) - 1]

    def isEmpty(self):
        return len(self.items) == 0

    def printStack(self):
        for i in range(len(self.items)):
            print(self.items[i])


def main():
    s = Stack()


if __name__ == "__main__":
    main()
