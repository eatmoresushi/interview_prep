import timeit

# recursive
def fibonacci1(i):
    if i == 0 or i == 1:
        return i
    return fibonacci1(i - 1) + fibonacci1(i - 2)


# top-down dynamic
def fibonacci2i(i):
    return fibonacci2(i, [0] * (i + 1))


def fibonacci2(i, memo):
    if i == 0 or i == 1:
        return i
    if memo[i] == 0:
        memo[i] = fibonacci2(i - 1, memo) + fibonacci2(i - 2, memo)
    return memo[i]


# bottom-up dynamic
def fibonacci3(i):
    if i == 0:
        return 0
    a, b = 0, 1
    for _ in range(2, i):
        c = a + b
        a = b
        b = c
    return a + b


def main():
    print(timeit.timeit("fibonacci1(10)", globals=globals()))
    print(timeit.timeit("fibonacci2i(10)", globals=globals()))
    print(timeit.timeit("fibonacci3(10)", globals=globals()))


if __name__ == "__main__":
    main()
