A = [1,2,3,4,5,6,6,77,55,33,23,45,65,45]
# even =[]
# odd = []

# for element in A:
#     if element % 2 == 0:
#         even.append(element)
#     else:
#         odd.append(element)
# print(odd)
# print(even)

C = [element + 2 for element in A]
print(C)
even=[element for element in A if element%2==0]
odd=[element for element in A if element%2!=0]
print(even)
print(odd)


D = [-1,2,-4,3,4,5,-8,-3,0,8,5,7,-6]
pstv = [element for element in D if element>0]
negt = [element for element in D if element<0]
print(pstv,negt)

pstv.sort()
print(pstv)

temp_value=pstv[0]
for element in pstv:
    if element > temp_value:
        temp_value = element
    max_value = temp_value
print(max_value)

print(len(negt))
