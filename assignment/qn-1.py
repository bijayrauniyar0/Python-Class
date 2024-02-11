#check number is positive negative or zero

def check_number(num):
    if num > 0:
        print(f"{num} is positive")
    elif num < 0:
        print(f"{num} is negative")
    else:
        print(f"{num} is zero")

number=int(input("Enter a number:\t"))
check_number(number)