def check_prime(num):
    c=0
    prime=False
    for i in range(1,num+1):
        if num%i==0:
            c=c+1
    if c==2:
        prime=True
    return prime

def get_multipication_table(num): #def is to define custom function
    for i in range(1,11):   #loop
        print(f"{num}*{i}={num*i}")

number=int(input("Enter a number to get multipication table: \t"))

if check_prime(number):
    get_multipication_table(number)


