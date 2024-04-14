def multiply(x, y):
    result = x * y
    return result


def is_palindrome(string):
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence):
    result = ""
    for char in sentence:
        if char.isalnum():
            result += char
    return is_palindrome(result)


# word = input("Please enter a word to check: ")
# if is_palindrome(word):
#     print(f"'{word}' is a palindrome!")
# else:
#     print(f"'{word}' is not a palindrome.")

sentence = input("Please enter a sentence to check whether it is a paolindrom or not: ")
if palindrome_sentence(sentence):
    print(f"'{sentence}' is a palindrome sentence.")
else:
    print(f"'{sentence}' is not a palindrome sentence.")


# answer = multiply(10.5, 4)
# print(answer)

# forty_two = multiply(6, 7)
# print(forty_two)

# print()

# for val in range(1, 5):
#     two_times = multiply(2, val)
#     print(two_times)
