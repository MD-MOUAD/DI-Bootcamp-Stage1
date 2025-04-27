#!/usr/bin/env python3

# Task 1: Print out all the values in the list one by one.
lst1 = [1, 2, 3, 4]
for value in lst1:
  print(value)

# Task 2: Print out all the values in the list multiplied by 20.
for value in lst1:
  print(value * 20)

# Task 3: Return a new list with only the first letter of each name.
names = ["Elie", "Tim", "Matt"]
first_letters = [name[0] for name in names]
print(first_letters)

# Task 4: Return a new list with all the even values.
lst2 = [1, 2, 3, 4, 5, 6]
even_values = [value for value in lst2 if value % 2 == 0]
print(even_values)

# Task 5: Return a new list that contains only the values present in both lists.
lst3 = [1, 2, 3, 4]
lst4 = [3, 4, 5, 6]
common_values = [value for value in lst3 if value in lst4]
print(common_values)

# Task 6: Return a new list with each word reversed and in lowercase.
words = ["Elie", "Tim", "Matt"]
reversed_words = [word.lower()[::-1] for word in words]
print(reversed_words)

# Task 7: Return a new list of the letters that are present in both strings.
str1 = "first"
str2 = "third"
common_letters = [char for char in str1 if char in str2]
print(common_letters)

# Task 8: Return a list of the numbers that are divisible by 12 between 1 and 100.
divisible_by_12 = [i for i in range(1, 101) if i % 12 == 0]
print(divisible_by_12)

# Task 9: Return a list with all the vowels removed from the string "amazing".
string = "amazing"
vowels = "aeiou"
no_vowels = [char for char in string if char not in vowels]
print(no_vowels)

# Task 10: Generate a list with the following value: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
list_1 = [[0, 1, 2] for _ in range(3)]
print(list_1)

# Task 11: Generate a list with the following structure.
list_2 = [[i for i in range(10)] for _ in range(10)]
print(list_2)
