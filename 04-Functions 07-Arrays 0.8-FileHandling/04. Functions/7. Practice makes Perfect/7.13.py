###
# Numbers from 1 to n string

def f(n):
    str_num = ""
    for i in range(1, n+1):
        str_num += str(i)
    return str_num

numa = int(input('Enter a number: '))
print(f'{f(numa)}')