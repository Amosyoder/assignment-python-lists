
# Task 1: Use a list comprehension to create a new list containing only even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even Numbers:",even_numbers)

# Task 2: Use a list comprehension to create a new list containing numbers greater than 5
greater_than_five = numbers = [num for num in numbers if num > 5]
print("Greater than five:",greater_than_five)

# Task 3: Check if the number 7 is in the original numbers list
if 7 in numbers:
    print("7 is in the original number list")
else:
    print("7 is not in the original number list")