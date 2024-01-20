for i in range(10):
    print (i)
# range is specified for loop and colon is given
print() #to provide line break

for i in range(1, 10):
    print (i)
print()

for i in range(1, 10, 2):  #1 is starting, 10 is end of range and 2 is addition/ skipping / jumping of i
    print (i)

#checking prime
    c=0
#a=input("enter a number") 
#throws string datatype
b=int(input("enter a number"))
for i in range(1, b+1):
    if(b%i == 0):
        c=c+1
if c == 2:
    print("number is prime")
else:
    print("not prime")


