x = ("hello", 1212, 12, "cool", 4, 1, "x", 5, 4, 3)
y = (12, 14, 1, 51, 214, 2, 1231, 2, 1)

q = x.count(4)
w = y.count(2)
print(q, w)

r = x + y
print(r)  # concatenated

r = x * 2
print(r)  # replicate

print("cool" in x)  # check the value is exist or not
print(2 in y)

print(len(x))


# practise


# x = []

# q = input("Enter The Fruit Name:- ")
# x.append(q)

# w = input("Enter The Fruit Name:- ")
# x.append(w)

# e = input("Enter The Fruit Name:- ")
# x.append(e)

# r = input("Enter The Fruit Name:- ")
# x.append(r)

# t = input("Enter The Fruit Name:- ")
# x.append(t)

# y = input("Enter The Fruit Name:- ")
# x.append(y)

# u = input("Enter The Fruit Name:- ")
# x.append(u)

# print(x)


x = []

q = int(input("Enter The marks Name:- "))
x.append(q)

w = int(input("Enter The marks Name:- "))
x.append(w)

e = int(input("Enter The marks Name:- "))
x.append(e)

r = int(input("Enter The marks Name:- "))
x.append(r)

t = int(input("Enter The marks Name:- "))
x.append(t)

y = int(input("Enter The marks Name:- "))
x.append(y)

u = int(input("Enter The marks Name:- "))
x.append(u)

x.sort()
print(x)
print(sum(x))
