#!/usr/bin/env python3

# Task 1: Given a list of tuples, create a dictionary.
list1 = [("name", "Elie"), ("job", "Instructor")]
dict1 = dict(list1)
print(dict1)  # Output: {'name': 'Elie', 'job': 'Instructor'}

# Task 2: Given two lists, create a dictionary mapping elements from the first list to elements from the second.
list2 = ["CA", "NJ", "RI"]
list3 = ["California", "New Jersey", "Rhode Island"]
dict2 = dict(zip(list2, list3))
print(dict2)  # Output: {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}

# Task 3: Create a dictionary with vowels as keys and 0 as values.
vowels = ['a', 'e', 'i', 'o', 'u']
dict3 = {}
for vowel in vowels:
  dict3[vowel] = 0
print(dict3)  # Output: {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

# Task 4: Create a dictionary where the key is the position of the letter in the alphabet, and the value is the letter.
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
dict4 = {}
for i in range(26):
  dict4[i + 1] = alphabet[i]
print(dict4)

# Super Bonus: Given the string "awesome sauce", create a dictionary with vowels as keys and their counts as values.
text = "awesome sauce"
vowel_count = {}
for vowel in 'aeiou':
  vowel_count[vowel] = text.count(vowel)
print(vowel_count)  # Output: {'a': 2, 'e': 3, 'i': 0, 'o': 1, 'u': 1}
