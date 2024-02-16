def upChar(str):
    new_str = str.upper()
    return new_str

def func_upper(word):
    if word.startswith("c"):
        a = word.title()
    else:
        a =word.upper()
    return a

# lamda function is defined in one line and below is shown
upper_string_lambda = lambda x : x.upper()

sentence = input("Enter a sentece:\t")
# print(upChar(sentence))
splitted_data = sentence.split(" ")


# final_ans = list(map(func_upper, splitted_data))
# final_ans = list(map(upper_string_lambda, splitted_data))
# print(final_ans)


def func_upper2(word,index):
    if index % 2 == 0:
        a = word.title()
    else:
        a =word.upper()
    return a


result = [func_upper2(word,index) for index,word in enumerate(splitted_data)]
print(" ".join(result))


# for x, y in enumerate(list)
# print(x,y)
