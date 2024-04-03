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
        print(f"Adding {current_choice}")
        index = int(current_choice) - 1
        chosen_part = available_part[index]
        computer_parts.append(chosen_part)

    else:
        print("Please add options from the list below:")
        for number, part in enumerate(available_part):
            print(f"{number + 1}: {part}")

    current_choice = input()

print(computer_parts)
