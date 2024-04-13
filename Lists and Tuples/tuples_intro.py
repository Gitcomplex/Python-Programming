# t = ("a", "b", "c")
# print(type(t))

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bud = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])
print()

# metallica[0] = "Master of Puppets"
# tuples uses less memory than lists
# tuples protect the intergrity of our data

metallica2 = list(metallica)
print(metallica2)

metallica2[0] = "Master of Puppets"
print(metallica2)
