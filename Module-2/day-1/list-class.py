a = [91,2,3,5,2,4,1,2,6,5,5,"hello", True]
#a = (91,2,3,4,5,"hello", True) #tuple does't have append attrib
a.append("bijay")

print(type(a)) #prints what type of data is a holding
print(a[-1]) #prints data in index -1

print(a.pop()) #displays popped element
#a.pop() ,removes/pops the element

print(a)
print(a.index(2)) #displays the index of element
print(a.index(2,3)) 
#2 is the element to be searched and 3 is the starting of index i.e 2 is searched from index 3

a.insert(3,"rauniyar") #adds rauniyar to index 3
print(a)

a.insert(a.index(2),False) #pushs the element 2 and inserts False
print(a)
a.insert(a.index(2),"bijay")
print(a)

a.remove(2) #removes the first available element i.e 2
print(a)

a.reverse() #reverse the whole list
print(a)

print(a[1:3]) #prints the value from index 1 to 7-1
b = a[2:6] #holds the sliced data
b = a[2:-6] #holds the sliced data
b = a[:6] #holds data before index 6
b = a[6:] #holds data after index 6
b = a[:7:2] #starts from 0 index to index 7 and skips 1 element
print(b)

c = a[::2] #holds element with even index
print(c)
print(len(a)) #displays the length of a
print(a.count(2)) #displays no of 2's in the list

e=[1,5,2,9,6,7,3,4,5,6,7,8,8,6,43,24,11]
e.sort() #sorts the data
print(e)

f=["bijay","rauniyar","bca"]
g=f.copy() #copies the data of f to b
f.sort()
print(f)
print(g)