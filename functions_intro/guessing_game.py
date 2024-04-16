import random


def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        #else: is not needed
        print(f"{temp} is not a valid number: Please try again.")


highest = 10
answer = random.randint(1, highest)
print(answer)  # TODO: Remove after testing
guess = 0  # initialised guess
print(f"Please guess a number between 1 and {highest}: ")

while guess != answer:
    guess = get_integer(": ")

    if guess == 0:
        print("Quitting the Game")
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:  # guess must be greater than answer
            print("Please guess lower")


# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")

# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")

# else:
#     print("You got it first time")
