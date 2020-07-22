def reverse_func(seq):
    seqType = type(seq)
    # if we write str() or list() we get an empty string or list respectively
    emptyseq = seqType()

    def reverse_main(seq):
        if seq == emptyseq:
            return emptyseq

        first = seq[0: 1]
        base = seq[1:]

        return reverse_main(base) + first

    return reverse_main(seq)


def main():
    print(reverse_func([1, 2, 3, 4, "hello"]))
    print(reverse_func("hello"))


if __name__ == "__main__":
    main()
