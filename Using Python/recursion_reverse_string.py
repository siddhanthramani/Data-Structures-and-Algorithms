def reverse(l):

    if(l == ""):  # cannot use single quotes, only double quotes
        return ""
    # getting the elements from index 1 to end
    first = l[0: 1]
    return reverse(l[1:]) + first


def main():

    a = input('Enter the string : ')
    print(reverse(a))


if __name__ == "__main__":
    main()
