###
#
#
def f(expression):
    total = 0
    currentnum = 0
    sign = 1 #1 for positive numbers and -1 for negative numbers
    for char in expression:
        if char.isdigit():
            currentnum = int(char)
            total += sign * currentnum
        elif char == "+":
            sign = 1
        elif char == "-":
            sign = -1
    return total

expression = input("Enter an arithmetical expression: ")
print(f'The total value of your expression is: {f(expression)}')
        
         
