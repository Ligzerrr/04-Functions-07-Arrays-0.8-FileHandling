###
# Prime number checker
#
def f(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 2
    return True

numbe = int(input('Enter which prime number you would like to see: '))
count = 0
n2 = 2
while count < numbe:
    if f(n2):
        count += 1
    n2 += 1
print(f'{n2}')

