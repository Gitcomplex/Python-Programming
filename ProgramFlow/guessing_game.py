import random

highest = 10
answer = random.randint(1, highest)
print(answer)  # TODO: Remove after testing


print(f"Please guess a number between 1 and {highest}: ")
guess = int(input())
if guess == answer:
    print("You've guessed it first time")
else:
    while guess != answer:
        if guess == 0:
            print("Quitting the Game")
            break
        if guess < answer:
            print("Please guess higher")
        else:  # guess must be greater than answer
            print("Please guess lower")
        guess = int(input())
        if guess == answer:
            print("Well done, you guessed it")
        else:
            print("Sorry, you have not guessed correctly")


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
