###
# Program that returns a months name based on its number indicator
#
import month

def main():
    month_name = month.month(int(input('Enter your selected month (1-12): ')))
    print(f"The name of the month you've entered is: {month_name}")

if __name__ == "__main__":
    main()
