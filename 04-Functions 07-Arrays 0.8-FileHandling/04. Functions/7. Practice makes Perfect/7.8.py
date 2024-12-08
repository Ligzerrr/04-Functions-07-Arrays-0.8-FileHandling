###
# Program that returns the minimum number of coins that can be used to pay for the purchased product
#

def f(amount_to_pay):
    count_coin = 0
    
    count_coin += amount_to_pay // 5 #Dzielenie z zaokragleniem
    amount_to_pay %= 5
    
    count_coin += amount_to_pay // 2
    amount_to_pay %= 2
    
    count_coin += amount_to_pay // 1
    amount_to_pay %= 1
    return count_coin

price = int(input('Enter the price: '))
print(f'The amount of coins needed for the payment: {f(price)}')
        