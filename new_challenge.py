# def menu():
#     print("Please choose your option from the list below:")
#     print("1:\tLean Python")
#     print("2:\tLearn Java")
#     print("3:\tGo Swimming")
#     print("4:\tHave Dinner")
#     print("5:\tGo to bed")
#     print("0:\tExit")


# menu()
choice = "-"
while True:
    if choice == "0":
        break
    elif choice in ["1", "2", "3", "4", "5"]:
        print(f"You choose {choice}")
    else:
        print("Please choose your option from the list below:")
        print("1:\tLean Python")
        print("2:\tLearn Java")
        print("3:\tGo Swimming")
        print("4:\tHave Dinner")
        print("5:\tGo to bed")
        print("0:\tExit")
