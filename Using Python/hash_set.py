class HashSet:
    def __init__(self, contents=[]):
        self.items = [None] * 10
        self.numItems = 0

        for item in contents:
            self.add(item)

    # to achieve amortized complexity of O(1), we keep making a new list once the load factor
    # of current list becomes greater than 0.75, where load factor tells us how many places are the
    # in the list and is defined as the ratio of no of not none elements by the length of the list.
    # Creating a new Hash list is done with the rehash function
    def __rehash(self, oldList, newList):
        for x in oldList:
            # get all the filled indexes of the list
            if x != None and type(x) != HashSet.__Placeholder:
                HashSet.__add(x, newList)
        return newList

    # this is the HashSet add helper function
    def __add(self, item, items):

        # we divide and get remainder to ensure the idx is between 0 and the max index of the list
        idx = hash(item) % len(items)
        loc = -1  # default value of loc (no index list has this value)

        # while we do not enter a location which has a none value
        while items[idx] != None:
            if items[idx] == item:
                # item already in set
                return False
            # if we run into a placeholder while scanning NOT none values, location is set as that
            # only the first placeholder vaue will be transferred as loc will change and will not
            # enter the loop for other placeholders as loc < 0 will not hold true
            if loc < 0 and type(items[idx]) == HashSet.__Placeholder:
                loc = idx

            # we will keep increasing the index and diciding it by len of the list
            idx = (idx + 1) % len(items)

        # if no placeholder was found, the first none valued index will be the loc
        if loc < 0:
            loc = idx

        # moving the value of item to particular location in the list
        # if no  placeholders or no emty places in list are found, loc is -1 and the
        # value will not be added to the list. loc will however never be -1 because we keep
        # increasing the length of the list
        items[loc] = item

        return True

    # the add function uses the helper add and helper hash functions.
    def add(self, item):
        # we will add element to list using helper add function
        if HashSet.__add(item, self.items):

            # if add returns true, increment no of elements in list
            self.numItems += 1
            # find new load factor
            load = self.numItems / len(self.items)
            # if load is greater than thresh, rehash to maintain amortized comp for adding a
            # value to the list is O(1)
            if load >= 0.75:
                self.items = HashSet.__rehash(
                    self.items, [None] * 2 * len(self.items))
                # we increase the length of the hash list by two times

    # the placeholder class is used as a value when the an element in the list is deleted
    # this is used and not None in most cases as it will be easier to traverse the list
    class __Placeholder:
        def __init__(self):
            pass

        def __eq__(self, other):
            return False

    # this helper function is used to remove an element from the Hash List
    def __remove(self, item, items):

        # the first idx will no be less than the hash value by len of lists
        # cause that is how they have been defined
        idx = hash(item) % len(items)

        while items[idx] != None:
            if items[idx] == item:
                nextIdx = (idx + 1) % len(items)
                # if the last element is the one being deleted, replace with None
                if items[nextIdx] == None:
                    items[idx] = None
                # if any other element is deleted, replace with the placeholder function
                else:
                    items[idx] = HashSet.__Placeholder()

                return True
            idx = (idx + 1) % len(items)

        # if the element does not exist
        return False

    def remove(self, item):
        if HashSet.__remove(item, self.items):
            self.numItems -= 1
            load = max(self.numItems) / len(self.items)
            # if the load value is lesser than 0/25, it is an inefficient use of space(memory)
            # and hence we reduce the list size by a factor of 2
            if load <= 0.25:
                # the int casting is done to convert float to int
                self.items = HashSet.__rehash(
                    self.items, [None] * int(len(self.items)/2))
        else:
            raise KeyError("Item not in HashSet")

    # HashSet Membership
    def __contains__(self, item):
        # the first idx will no be less than the hash value by len of lists
        # cause that is how they have been defined
        idx = hash(item) % len(self.items)

        while self.items[idx] != None:
            if self.items[idx] == item:
                return True

            idx = (idx + 1) % len(self.items)

        return False

    def __iter__(self):
        for i in range(len(self.items)):
            if self.items[i] != None and type(self.items[i]) != HashSet.__Placeholder:
                # yielding will keep returning values instead of returning one value and
                # then stopping
                # After returning the value, the execution resumes from after the yield value
                yield self.items[i]
