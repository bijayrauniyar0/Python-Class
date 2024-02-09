# songs = {
#     "aashiqui":"arijit",
#     "tu mujhe soch kabhi" : "kk"
# }
# print(songs["aashiqui"])
# print(songs.values())
# songs.pop('aashiqui') 
# # pops the item with key named aashiqui
# print (songs)

# songs["meri aashiqui"] = "Jubin Nautiyal" 
# # adds the items
# print (songs)

# songs.popitem()
# print(songs)


# student = {
#     "name": "John",
#     "age": 30,
#     "subjects":["math", "Science", "History"],
#     "address": {
#         "street": "123 Main St",
#         "city": "Anytown",
#         "state": "CA",
#         "zip_code": "12345"
#         }   

# }
# print(student["address"]["city"])
# # loop for getting keys and values

# for values in student.values():
#     print (values)
# for keys in student.keys():
#     print(keys)
# print(student.get("name"))

marks = {
    "bijay" : 98,
    "abhinab" : 45,
    "jenish" : 72,
    "jack" : 79,
    "John" : 58,
}
# top_students = {}
# odd = {}
# even = {}
# zero = {}
# for keys,values in marks.items():
#     if values > 70:
#         top_students[keys] = values
# print(top_students)

# for keys,values in marks.items():
#     if values % 2 != 0:
#         odd[keys] = values+1
#     elif values % 2 == 0:
#         even[keys] =  values+1
#     else:
#         zero[keys] = values+1

# print(odd)
# print(even)
# print(zero)

# my_dict = {key:value for key,value in marks.items() if value>70}
#does thww work of for loop

# print (my_dict)
new_marks = {}
for key, values in marks.items():
    if key[0] == "j":
        new_marks[key] = values/2

print(new_marks)

low = {key.lower():value/2 for key,value in marks.items()}
print(low)

# key.startswith("j") check if initail letter starts with j
sec_dict = {key:value/2 for key,value in low.items() if key.startswith("j")}
# if key[0] == "j"
print(sec_dict)
    
