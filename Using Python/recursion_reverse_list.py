def reverse(l):

    if(l == []):
        return []
    # getting the elements from index 1 to end
    first = l[0: 1]
    return reverse(l[1:]) + first


def main():

    a = []
    len = int(input('Enter the no size of list : '))

    # gets the elemennts in the list from the user
    for i in range(0, len):
        a.append(input('Enter element : '))

    a = reverse(a)

    print(a)


if __name__ == "__main__":
    main()
