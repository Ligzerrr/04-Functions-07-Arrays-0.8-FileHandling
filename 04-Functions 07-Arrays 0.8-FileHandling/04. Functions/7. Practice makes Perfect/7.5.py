###
# Program that checks if a number is within a select range
#
import numrange
def main():
    num = int(input('Enter the number you selected: '))
    x = int(input('Enter the first range endpoint: '))
    y = int(input('Enter the second range endpoint: '))
    does_appear = numrange.range_num(num,x,y)
    print(f'The number {num} is a part of the range <{x},{y}>: {does_appear}')
if __name__ == "__main__":
    main()


