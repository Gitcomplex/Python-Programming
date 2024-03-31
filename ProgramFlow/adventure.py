available_gates = ["North", "South", "East", "West"]

choosen_exit = ""
while choosen_exit not in available_gates:
    choosen_exit = input("Please choose a gate: ").capitalize()
    if choosen_exit == "Quit" or "quit":
        print("***************GAME OVER*****************")
        break
else:
    print("Aren't you glad you got out of there")
