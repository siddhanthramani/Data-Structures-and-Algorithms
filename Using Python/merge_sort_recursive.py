import random


# assume in a list of size 8, you have the first four and last four sorted, if we
# can then figure out an algo which can sort the entire list, we will be able to do the merge sort
# recursively as we can sort the first four assumning the first two and last two are sorted and so on
# till we have only single elemets which are sorted by default.

# the algo which we spoke of before (figure out an algo) is the merge function written below


def merge(seq, start, mid, stop):
    lst = []
    i = start
    j = mid

    # we compare the values of the list in order to merge sorted lists into a bigger sorted list
    # i is for the first sorted list and j is for the second sorted list
    while i < mid and j < stop:
        if seq[i] < seq[j]:
            lst.append(seq[i])
            i += 1
        else:
            lst.append(seq[j])
            j += 1
    # in case all the j index values are appended but some of i index still remain, they
    # will just be appended as they are
    while i < mid:
        lst.append(seq[i])
        i += 1

    # the above thing has to be done in case i index is fully appended and j index remains
    # but we do not do that
    # while j < stop:
    #     lst.append(seq[j])
    #     j += 1
    # but that is not required cause it is taken care of (done automatic) when we copy the values
    # from the append list to the original sequence
    # for the i list this will not be done automatically done. therefore, we have to specify it
    # separately

    # copies only (in ref to above comments) appended values to the new list
    for i in range(len(lst)):
        seq[start+i] = lst[i]

    return seq


def merge_sort_recursive(seq, start, stop):

    # the greater than symbol is used in case we input an empty list
    # otherwise == will work fine
    if start >= stop-1:
        return
    # this gets the value of the middle value floored (rounded to lower integer)
    mid = (start + stop) // 2

    # this keeps running recursive till the first to mid values are sorted
    merge_sort_recursive(seq, start, mid)
    # this keeps running recursive till the mid to stop values are sorted
    merge_sort_recursive(seq, mid, stop)

    # this will merge the two lists
    return merge(seq, start, mid, stop)


# this function calls the first recursion of the sort function
def merge_sort(seq):

    # randomising is NOT required
    # we are doing this to ensure the algo works for many different combinations
    for i in range(len(seq)):
        j = random.randint(0, len(seq) - 1)
        temp = seq[j]
        seq[j] = seq[i]
        seq[i] = temp

    print(seq)

    return merge_sort_recursive(seq, 0, len(seq))


def main():

    print(merge_sort([5, 4, 3, 2, 1, 9, 8, 7, 6]))


if __name__ == "__main__":
    main()
