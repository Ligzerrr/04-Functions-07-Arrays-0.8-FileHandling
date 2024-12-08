###
# Calculator program

def f(n1,n2,op):
    ski = 0
    if op == "+":
        ski = n1 + n2
    elif op == "-":
        ski = n1 - n2
    elif op == "*":
        ski = n1 * n2
    elif op == "%":
        ski = n1 % n2
    elif op == "**":
        ski = n1 ** n2
    return ski
        
num1 = int(input('Enter your first number: '))
num2 = int(input('Enter your second number: '))
oper = input('Enter your operator: ')

print(f'{f(num1,num2,oper)}')