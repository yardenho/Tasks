# regular recursive
def summer(num):
    if num == 0:
        return 0
    return summer(num//10) + num % 10


# tail cell recursive
def tailCellRecursiveSummer(num, b):
    if num == 0:
        return b
    return tailCellRecursiveSummer(num//10, b + num % 10)
