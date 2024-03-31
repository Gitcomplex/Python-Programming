low = 1
high = 1000

print(f"Please think of a number between {low} and {high}: ")
input("Please ENTER to start")

guesses = 1

while low != high:
    guess = low + (high - low) // 2
    high_low = input(
        f" My guess is {guess} Should I guess higher or lower? Enter h, l or c, If my guess is Correct"
    ).casefold()

    if high_low == "h":
        low = guess + 1

    elif high_low == "l":
        high = guess - 1

    elif high_low == "c":
        print(f"I got it {guesses} guesses!")
        break

    else:
        print("Please Enter h, l or c")

    guesses += 1

else:
    print(f"You thought of the number {low}.")
    print(f"I got it in {guesses} guesses.")
