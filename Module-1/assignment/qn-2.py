# to check if the year is leap or not

def check_leap(num):
    if num % 4 == 0 and num % 100 != 0:
        print(f"{num} is a leap year")
    elif num % 400 == 0:
        print(f"{num} is a leap year")
    else:
        print(f"{num} is not a leap year")

year = int(input("Enter year to check:\t"))
check_leap(year)