

# A linked list consisting of three pieces of information. We keep a
# reference to the ﬁrst node in the sequence so we can traverse the nodes when necessary.
# The reference to the last node in the list makes it possible to append an item
# to the list in O(1) time. We also keep track of the number of items
# so we don’t have to count when someone wants to retrieve the list size.

# Finally, the sort operation is not applicable on linked lists.
# Efﬁcient sorting algorithmsrequirerandomaccesstoalist.
# Insertionsort,aO(n2)algorithm,wouldwork, but it would be highly inefﬁcient.
# If sorting were required, it would be much more efﬁcient to copy the linked list to
# a randomly accessible list, sort it, and then build a new sorted linked list
# from the sorted list.


class LinkedList:

    # this can be used internally only by the linked list and not by the user as it has only
    # 2 underscores preceding it. If it is followed by 2 underscores also, then it
    # becomes an operator name
    # In the Node class there are two pieces of information: the item is a reference to a
    # value in the list,and the next reference which points to the next node in the sequence

    class __Node:

        # this inits the new node and sets the value of the node(item) and the object it points to (next)
        # the object it points to is the next node
        def __init__(self, item, next=None):
            self.item = item
            self.next = next

        # this returns the value of the current node
        def getItem(self):
            return self.item
        # this returns the address of the next node

        def getNext(self):
            return self.next
        # this sets the value of the current node. Used for updation

        def setItem(self, item):
            self.item = item
        # this sets the reference to the next node. Used for updation

        def setNext(self, next):
            self.next = next

    def __init__(self, contents=[]):
        # Here we keep a reference to the first and last node.
        # Both point to a dummy node initially.
        # A dummy node is important as it can help circumventing problems and elminating many
        # many special cases which arise if not for a dummy node

        # reference to the start (self.first) is also called head
        # both first and last are nodes by themselves

        # this refers to the same values that first node refers to
        self.first = LinkedList.__Node(None, None)
        # this refers to the same values that the last node refers to
        self.last = self.first
        # It is useful to have the no of nodes in the LL
        self.numItems = 0

        for e in contents:
            self.append(e)

    def __getitem__(self, index):
        if index >= 0 and index < self.numItems:
            cursor = self.first.getNext()
            for i in range(index):
                cursor = cursor.getNext()

            return cursor.getItem()

        raise IndexError("Linked List index out of range")

    def __setitem__(self, index, val):
        if index >= 0 and index < self.numItems:
            cursor = self.first.getNext()

            for i in range(index):
                cursor = cursor.getNext()

            cursor.setItem(val)
            return

        raise IndexError("Linked List assignment index out of range")

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Concatenate undefine for " +
                            str(type(self)) + "+" + str(type(other)))
        # the single / is an escape sequence which will trim all whitespaces to one space
        result = LinkedList()

        cursor = self.first.getNext()  # cursor is a node too
        while cursor != None:
            result.append(cursor.getItem())
            cursor = cursor.getNext()

        cursor = other.first.getNext()
        while cursor != None:
            result.append(cursor.getItem())
            cursor = cursor.getNext()

        # Notice how the dummy nodes of both the lists where not added to the result
        # whereas the result will have dummy node when the result is initialized
        return result

    def append(self, item):
        node = LinkedList.__Node(item)
        # since self.last points to the last node, we make the
        self.last.setNext(node)
        # previous last node point to the new last node
        self.last = node  # we then have refer the new last node
        self.numItems += 1

    def insert(self, index, item):
        cursor = self.first

        if index < self.numItems:
            for i in range(index):
                cursor = cursor.getNext()
            # cursor now refers to the node before the place where new node is to be inserted
            # (the preceding node)
            # new node points to what the cursor is pointing to
            # this is done before next step so that we do not lose the value of preceding node's
            # getNext()
            node = LinkedList.__Node(item, cursor.getNext())
            # the cursor is made to point at the new node
            cursor.getNext(node)
            self.numItems += 1

        else:
            self.append(item)

    def __delitem__(self, index):

        cursor = self.first

        for i in range(index):
            cursor = cursor.getNext()
        # cursor now points to the node preceding the one to be deleted

        # the preceding nodes should point to the node the about to be deleted node points to
        cursor.getNext(cursor.getNext().getNext())

        # drop cursor.getNext()
        cursor = cursor.getNext()
        del cursor
