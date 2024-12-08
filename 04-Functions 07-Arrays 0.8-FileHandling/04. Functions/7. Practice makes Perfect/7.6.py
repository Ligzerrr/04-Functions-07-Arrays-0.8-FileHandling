###
# Program that hides credit card numbers
#
import hidecard

card = input('Enter your card number')
print(f'The credit card number after masking is: {hidecard.hide(card)}')