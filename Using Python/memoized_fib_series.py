mem_fib = {}
mem_fib[0] = 0
mem_fib[1] = 1


def fib(n):

    if n in mem_fib:
        return mem_fib[n]

    val = fib(n-1) + fib(n-2)
    mem_fib[n] = val

    return val


def main():
    try:
        n = int(input("No of fib values : "))
    except:
        raise TypeError("Enter only +ve integers.")
    print(fib(n))


if __name__ == "__main__":
    main()
