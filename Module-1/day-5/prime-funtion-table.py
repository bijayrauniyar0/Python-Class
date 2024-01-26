import sys 
sys.path.insert(1, '../../') #this specifies the path, currently it took me to Parent-folder

from Models.module import*


number=int(input("Enter a number:\t"))

# if not check_prime(number):
if check_prime(number):
    function_x(number)
else:
    get_multipication_table(number)

#from models-try.module-5 import* #we can directly import module if the module is in same dir
from modelsTry.module5 import*

number=5
check_odd_even(number)
