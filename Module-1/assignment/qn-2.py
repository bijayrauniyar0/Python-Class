# to check if the year is leap or not

def check_leap(year):
    if year % 4 == 0 and year % 100 != 0:
        print(f"year {year} is a leap year")
    elif year % 400 == 0:
        print(f"year {year} is a leap year")
    else:
        print(f"year {year} is not a leap year")

year = int(input("Enter year to check:\t"))
check_leap(year)