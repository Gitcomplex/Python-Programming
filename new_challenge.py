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
while choice != "0":
    if choice in "12345":
        print(f"You choose {choice}")
    else:
        print("Please choose your option from the list below:")
        print("1:\tLean Python")
        print("2:\tLearn Java")
        print("3:\tGo Swimming")
        print("4:\tHave Dinner")
        print("5:\tGo to bed")
        print("0:\tExit")
