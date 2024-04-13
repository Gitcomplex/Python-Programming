a = b = c = d = e = f = 12
print(c)

x, y, z = 1, 2, 76
print(x)
print(y)
print(z)

print("Unpacking a tuple")
data = 1, 2, 76  # data represents a tuple
x, y, z = data
print(x)
print(y)
print(z)

# we can unpack any sequence type
print("Unpacking a list")
data_list = [12, 13, 14]
#data_list.append(15)  # causes an error expected 4 values to unpack but got 3
p, q, r = data_list
print(p)
print(q)
print(r)

print("Unpacking a string")
s = "Hello"
a, b, c, d, e = s
print(a)
print(b)
print(c)
print(d)
print(e)


