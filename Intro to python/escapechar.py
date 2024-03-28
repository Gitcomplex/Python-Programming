splitString = "This string has been\nsplit over\nseveral\nlines"
print(splitString)

tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)

# we can use '\' to escape different characters
# for an instance we can escape quotes depending upon which ones we have used to enter strings

print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')
# or
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")

print("""The pet shop owner said "No, no, 'e's uh,...he's resting".""")

anotherSplitString  = """This string has been
split over
several
lines"""

print(anotherSplitString)

# we can escape the end of the line with a '\' character as well

anotherSplitString2  = """This string has been \
split over \
several \
lines"""

print(anotherSplitString2)

# how to escape the escape character 

print("C:\\Users\\Local\\notes.txt")
print(r"C:\Users\Appdata\notes.txt")
# r represent the use of raw string
