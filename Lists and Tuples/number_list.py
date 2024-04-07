empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# creating list by concatenating two lists
numbers = even + odd
print(numbers)

# #creating list by multiplying a list
# numbers = even * 3
# print(numbers)

# #creating list by using list() function
# numbers = list("123456789")
# print(numbers)

# creating list by using functions that return a list
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # creates a new list
print(numbers)

# creating a list from a string using sorted function
digits = sorted("432985617")
print(digits)
sorted_numbers_list = list(sorted_numbers)
print(sorted_numbers_list)

# creating list using list() function
digits = list("432985617")
print(digits)

# creating list using list() function and giving a list as an argument
more_number = list(numbers)
print(more_number)

# checking if 2 lists are same or not?
print(numbers is more_number)
print(numbers == more_number)

# copy() function demonstration
more_number = numbers.copy()
print(more_number)

# can also copy a list using a slice
more_number = numbers[:]
print(more_number)
# print(min(even))
# print(max(even))
# print(min(odd))
# print(max(odd))

# print()
# print(len(even))
# print(len(odd))

# print()
# print("mississippi".count("iss"))

# even.extend(odd)
# print(even)

# another_even = even
# print(another_even)

# even.sort(reverse=True)
# print(even)
# print(another_even)  # Since lists are mutable thus we only have one list here
