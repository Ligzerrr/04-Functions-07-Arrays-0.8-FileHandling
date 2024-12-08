def f(product_code):
    if len(product_code) != 4 or not product_code.isdigit():
        return False
    first_three_digits = product_code[:3]
    control_digit = int(product_code[3]) #splicing and index 
    sum_of_three = 0
    for digit in first_three_digits:
        sum_of_three += int(digit)
    return sum_of_three % 7 == control_digit #bool sprawdza czy suma trzech jest rowna control liczbie

code = input('Enter the product code: ')
print(f'Product code is correct: {f(code)}')
