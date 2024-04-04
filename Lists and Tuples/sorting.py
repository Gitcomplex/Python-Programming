pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
print(letters)

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers, reverse=False)
print(sorted_numbers)
print(numbers)

# since we're dealing with a list of numbers here, we can also use .sort() method

numbers.sort()
print(numbers)

missing_letter = sorted("The quick brown fox jumped over the the lazy dog")
print(missing_letter)
