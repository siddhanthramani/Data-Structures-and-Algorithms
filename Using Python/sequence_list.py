# the code is used to create a list and design the in built functions by ourselves
# Pylist is a wrapper class for the in-built list class
# A wrapper class is used to convert the inbuilt  primitive data type to an object datatype (in Java)

# the pylist constructor


class PyList:
    def __init__(self, contents=[], size=10):
        # the default value of contents is an empty list and the default
        # value of size is 10

        # to create a list of size items with value None
        self.items = [None] * size
        # num items is no of non None values of self. By default it is 0
        self.numItems = 0
        # self size is the total size of the list
        self.size = size
        # for the values in contents, transfer those values to the self
        for e in contents:
            self.append(e)

    # the inefficient append
    def append_ineff(self, item):
        self.items = self.items + item
        # the above is inefficient because every time we add an item, we create a new list and
        # then copy all the values of the previous list and the new value
        # the time complexity of this is n*(n+1)/2
        # or O(n2)

    def append_eff(self, item):
        self.items.append(item)
        # this just mutates the list to add one new element
        # to add n elements, it takes O(n) time only

    # the append function in python allows us to keep adding to a list while the size
    # of list keeps increasing. But internally, python is implemented in C
    # and in C, lists are arrays and they have a fixed length
    # i.e, you cant keep appending to a C array

    # the below method is an append method which shows how append in python must
    # be implemented if we assume python lists to have a fixed size
    def append(self, item):
        # when the no of elements is equal to the max size of self
        if self.numItems == len(self.items):
            # create a new list of twice the size (buffer space)
            newlst = [None] * 2 * self.numItems
            for k in range(len(self.items)):
                # copy the current elements of self to new list
                newlst[k] = self.items[k]
                # after the for loop is over, only the first numItems will be filled, others None

            # make self equal to the new list
            self.items = newlst

        self.items[self.numItems] = item  # append the new item

        self.numItems += 1  # increase count of elements

    # if we use double underscores in the start, the method is hidden and
    # is available ony for the class to use
    def __makeroom(self):
        newlen = 1

    # the below get and set item code is the actual code for the list
    # it is just shown for understanding purpose
    # since the methods are built in, they have 2 underscores both before and after them
    # ( ^ I think thats the reason)

    def __getitem__(self, index):
        if index >= 0 and index < self.numItems:
            return self.items[index]

        raise IndexError("Pylist index out of range")

    def __setitem__(self, index, val):
        if index >= 0 and index < self.numItems:
            self.items[index] = val
            return
        raise IndexError("PyList assignment index out of range")

    # to concatenate two lists
    def __add__(self, other):

        # creates new PyList with size = sum of size of both the lists
        result = PyList(size=self.numItems + other.numItems)

        for i in range(self.numItems):
            result.append(self.items[i])

        for i in range(other.numItems):
            result.append(other.items[i])

        # the complexity is O(n) where n is the sum of length of both lists

        return result


def main():
    sampleList = PyList([1, 2, 3])
    for i in range(10):
        print(sampleList.items[i])


if __name__ == "__main__":
    main()
