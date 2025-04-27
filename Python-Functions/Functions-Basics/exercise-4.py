#! /usr/bin/env python3

def sum_list(numbers):
  sum = 0
  for number in numbers:
    sum += number
  return sum


print(sum_list([1, 2, 3, 4]))
print(sum_list([5, 5, 5]))
