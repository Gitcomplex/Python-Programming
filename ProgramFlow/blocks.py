name = input("Please Enter your name: ")
age = int(input(f"How old are you,{name}:"))
print(age)

if age < 18:
    print(f"Please come back in {18-age} years.")
elif age == 900:
    print("Sorry, Yoda, you die in Return of the Jedi")
else:
    print("You are old enough to vote")
    print("Please put X in the box")