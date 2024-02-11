#counting words and turning them into dictionary
sentence = "bijay rauniyar loop loop verse bijay"
sentence_list = sentence.split()
dict_2 = {}

#normal method
for word in sentence_list:
    count =  sentence.count(word)
    dict_2[word] = count
print(dict_2)

#dictionary comprehension
dict_1 = {word:sentence.count(word) for word in sentence_list}



#counting letters in string and converting them to dictionary
# Get a sentence as input from the user
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Create a dictionary using dictionary comprehension
word_lengths = {word: len(word) for word in words}

# Print the resulting dictionary
print("Word lengths dictionary:")
print(word_lengths)
print(words)

#string reverse

def reverse_words(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Reverse each word and the overall sentence
    reversed_words = [word[::-1] for word in words][::-1]

    # Join the reversed words back into a sentence
    reversed_sentence = ' '.join(reversed_words)

    return reversed_sentence

# Example usage
sample_sentence = input("enter a sentence")
reversed_result = reverse_words(sample_sentence)

print(f"Original sentence: {sample_sentence}")
print(f"Reversed sentence: {reversed_result}")


