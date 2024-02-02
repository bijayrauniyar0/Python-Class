A = [1,2,3,4,5,6,6,77,55,33,23,45,65,45]
temp_value = A[0]
for element in A:
    if element > temp_value:
        temp_value = element
    max_value = temp_value
print(max_value)

