#! /usr/bin/env python3

human_years = int(input("Enter the number of human years: "))


rest = human_years - 2
if rest > 0:
    cat_years = 15 + 9 + (rest) * 4
    dog_years = 15 + 9 + (rest) * 5
else:
    cat_years = 15
    dog_years = 15

# Print the result
print([human_years, cat_years, dog_years])

"""
    This program calculates the age of a cat and a dog in their respective years
    based on the input human years.

    Args:
    human_years (int): The age of the pet in human years. This value must be >= 1.

    Returns:
    list: A list of three integers, representing:
      - The human years.
      - The equivalent cat years.
      - The equivalent dog years.
    
    Calculation Rules:
    - Cat Years:
      - 15 years for the first year.
      - 9 years for the second year.
      - 4 years for each year after the second year.
    - Dog Years:
      - 15 years for the first year.
      - 9 years for the second year.
      - 5 years for each year after the second year.
    
    Example:
    >>> calculate_pet_years(10)
    [10, 56, 64]
    
    >>> calculate_pet_years(1)
    [1, 15, 15]
    
    >>> calculate_pet_years(2)
    [2, 24, 24]
    """