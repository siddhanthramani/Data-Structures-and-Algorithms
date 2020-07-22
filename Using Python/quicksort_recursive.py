import random


def partition(seq, start, stop):
    pivotIndex = start
    pivotVal = seq[pivotIndex]

    for i in range(start+1, stop):

        # if the value is less than pivotval, we do a three number exchange
        # the value of the next location is stored in the lesser value index
        # the lesser value is stored in the index of current pivotval
        # the value of pivot val is stored in the next location

        if seq[i] < pivotVal:

            temp = seq[i]
            seq[i] = seq[pivotIndex + 1]
            seq[pivotIndex] = temp
            pivotIndex += 1
            seq[pivotIndex] = pivotVal

        print(seq)
        print('One it')
    print('\n\n')
    return (pivotIndex)


def quicksort_recursive(seq, start, stop):

    if start >= stop-1:
        return

    piv = partition(seq, start, stop)
    quicksort_recursive(seq, start, piv)
    if piv < len(seq)-1:
        quicksort_recursive(seq, piv+1, stop)

    return seq


def quicksort(seq):

    # randomising is required to be done on the pviot element every time
    # instead of that, we will do it on the list itself only once
    for i in range(len(seq)):
        j = random.randint(0, len(seq) - 1)
        temp = seq[j]
        seq[j] = seq[i]
        seq[i] = temp

    print(seq)

    return quicksort_recursive(seq, 0, len(seq))


def main():
    print(quicksort([5, 4, 3, 2, 1, 9, 8, 7, 6]))


if __name__ == "__main__":
    main()
