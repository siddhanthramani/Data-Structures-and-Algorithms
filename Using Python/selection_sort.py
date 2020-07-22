# Selection Sort is one of the early sorting algo but this is not what Pythons uses
# as the time comp is O(n2)


def select(seq, start):

    minIndex = start
    for i in range(start + 1, len(seq)):
        if(seq[minIndex] > seq[i]):
            minIndex = i

    return minIndex


def selection_sort(seq):
    for i in range(len(seq) - 1):
        minIndex = select(seq, i)
        temp = seq[i]
        seq[i] = seq[minIndex]
        seq[minIndex] = temp
    return seq


def main():
    print(selection_sort([5, 4, 3, 2, 1]))


if __name__ == "__main__":
    main()
