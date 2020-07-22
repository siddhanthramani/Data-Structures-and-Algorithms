# A queue is like a stack in many ways except that instead of being a LIFO
# data structure,queuesareFIFOorFirstIn/FirstOutdatastructures.
# The ﬁrst item pushed, is the ﬁrst item popped. When we are working with a queue we
#  talk of enqueueing an item, instead of pushing it. When removing an item from
# the queue we talk of dequeueing the item instead of popping it as we did from a stack.
# ThetableinFig.4.14 provides details of the queue operations and their complexities.
# Implementing a queue with the complexities given in this table is a bit trickier
# than implementing the stack.To implement a queue with these complexities we need to be able
#  to add to one end of a sequence and remove from the other end of the sequence
# in O(1) time. This suggests the use of a linked list. Certainly, a linked list
# would work to get the desired complexities. However, we can still use a list if
#  we are willing to accept an amortized complexity of O(1) for the dequeue operation.
# This Queue class code implements a queue with a list and achieves an
# amortized complexity of O(1) for the dequeue operation.


class Queue:
    def __init__(self):
        self.items = []
        self.frontIdx = 0

    def __compress(self):
        newlst = []

        # only the elements in the list are copied to the new list
        # the blank indexes before the first element are removed
        for i in range(self.frontIdx, len(self.items)):
            newlst.append(self.items[i])

        self.items = newlst
        self.frontIdx = 0

    def dequeue(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to dequeue an empty list")

        # when queue is half full, we compress it to ensure that we have an amortized complexity of
        # O(1) while not letting the queue grow unchecked
        # when we dequeue items, the front of the list is empty and vacant
        # so whenever the index of first element is at an index greater than the length / 2
        # we compress the list to achieve fast retrieval

        if self.frontIdx * 2 > len(self.items):
            self.__compress()

        item = self.items[self.frontIdx]
        self.frontIdx += 1
        return item

    def enqueue(self, item):
        self.items.append(item)

    def front(self):
        if self.isEmpty():
            return RuntimeError("Attempt to access front of empty queue. ")

        return self.items[self.frontIdx]

    def isEmpty(self):
        return self.frontIdx == len(self.items)
