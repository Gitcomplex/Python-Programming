available_part = [
    "Computer",
    "Monitor",
    "Keyboard",
    "Mouse",
    "Mouse mat",
    "HDMI Cable",
    "Webcam",
    "Microphone",
]

# valid_choices = [str(i) for i in range(1, len(available_part) + 1)] -> list comprehension
valid_choices = []
for i in range(1, len(available_part) + 1):
    valid_choices.append(str(i))
print(valid_choices)

current_choice = "-"
computer_parts = []  # created an empty list

while current_choice != "0":
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part = available_part[index]
        if chosen_part in computer_parts:
            print(f"Removing {current_choice}")
            computer_parts.remove(chosen_part)
        else:
            print(f"Adding {current_choice}")
            computer_parts.append(chosen_part)
        print(f"Your list now contains {computer_parts}")
    else:
        print("Please add options from the list below:")
        for number, part in enumerate(available_part):
            print(f"{number + 1}: {part}")

    current_choice = input()

print(computer_parts)

