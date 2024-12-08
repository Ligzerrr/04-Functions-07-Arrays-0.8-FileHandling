###
# Fibo

def f(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    fib1 = 0
    fib2 = 1
    helper = 0
    for i in range(n - 2):
        helper = fib2
        fib2 += fib1
        fib1 = helper
    return fib2

ent = int(input('Enter which value of the fib seq should be calculated: '))
print(f'{f(ent)}')

