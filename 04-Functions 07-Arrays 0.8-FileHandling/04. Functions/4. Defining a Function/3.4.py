###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    sum = 0
    str_cnvrsn = str(number)
    for i in range(len(str_cnvrsn)):
        sum += int(str_cnvrsn[i])
    return sum

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')