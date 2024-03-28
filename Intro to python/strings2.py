# strings are python seq data types
#                   1
#         012345678901234
parrot = "Norwegian Blue"



# print(parrot[0:6:2])
# print(parrot[0:6:3])

# number = "9,223;372:036 854,775;807"
# seperators = number[1::4]
# print(seperators)

# values = "".join(char if char not in seperators else " " for char in number).split()
# print([int(val) for val in values])

#print(parrot[3],parrot[4],parrot[9],parrot[3],parrot[6],parrot[8])

#use negative indexing
print(parrot[3-14],parrot[4-14],parrot[9-14],parrot[3-14],parrot[6-14],parrot[8-14])


