# 1. Declare a variable called first and assign it to the value "Hello World".
first = "Hello World"

# 2. Write a comment that says "This is a comment."
# This is a comment.

# 3. Log a message to the terminal that says "I AM A COMPUTER!"
print("I AM A COMPUTER!")

# 4. Write an if statement that checks if 1 is less than 2 and if 4 is greater than 2. If it is, show the message "Math is fun."
if 1 < 2 and 4 > 2:
  print("Math is fun.")

# 5. Assign a variable called nope to an absence of value.
nope = None

# 6. Use the language’s “and” boolean operator to combine the language’s “true” value with its “false” value.
result = True and False
print(result)  # Output: False

# 7. Calculate the length of the string "What's my length?"
length = len("What's my length?")
print(length)  # Output: 17

# 8. Convert the string "i am shouting" to uppercase.
shouting = "i am shouting".upper()
print(shouting)  # Output: "I AM SHOUTING"

# 9. Convert the string "1000" to the number 1000.
number = int("1000")
print(number)  # Output: 1000
print(type(number) ) # <class 'int'>

# 10. Combine the number 4 with the string "real" to produce "4real".
combined = str(4) + "real"
print(combined)  # Output: "4real"

# 11. Record the output of the expression 3 * "cool".
output = 3 * "cool"
print(output)  # Output: "coolcoolcool"

# 12. Record the output of the expression 1 / 0.
# print(1 / 0)  # ZeroDivisionError 

# 13. Determine the type of [].
print(type([]))  # Output: <class 'list'>

# 14. Ask the user for their name, and store it in a variable called name.
name = input("What is your name? ")
print(name)
# 15. Ask the user for a number. If the number is negative, show "That number is less than 0!"
# If positive, show "That number is greater than 0!" Otherwise, show "You picked 0!"
number = int(input("Enter a number: "))
if number < 0:
    print("That number is less than 0!")
elif number > 0:
    print("That number is greater than 0!")
else:
    print("You picked 0!")

# 16. Find the index of "l" in "apple".
index_l = "apple".index("l")
print(index_l)  # Output: 3

# 17. Check whether "y" is in "xylophone".
contain_y = "y" in "xylophone"
print(contain_y )  # Output: True

# 18. Check whether a string called my_string is all in lowercase.
my_string = "hello world"
is_lowercase = my_string.islower()
print(is_lowercase)  # Output: True