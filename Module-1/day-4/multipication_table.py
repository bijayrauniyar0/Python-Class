def get_multipication_table(num): #def is to define custom function
    for i in range(1,11):   #loop
        print(f"{num}*{i}={num*i}") # 5 * 1 = 5 .... so on
        
number=int(input("Enter a number to get multipication table: \t"))
get_multipication_table(number)

for i in range(number):
    get_multipication_table(i) 
    #in 2nd loop value of i from the loop is transfereed to num i.e num=i

    