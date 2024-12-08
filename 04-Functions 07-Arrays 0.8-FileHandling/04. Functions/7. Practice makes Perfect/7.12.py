###
# N asterisks string

def f(n):
    str_ast = "*"
    for i in range(1, n):
        str_ast += "/*"
    return str_ast

numbe = int(input('Enter a number: '))
print(f'{f(numbe)}')
    