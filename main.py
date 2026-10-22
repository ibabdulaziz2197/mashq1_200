# 1
x = 13
print(type(x))
print(x.bit_length())



# 2
s = "hello"
print(type(s))
print(s.upper())
print(s.replace("e", "3"))


# 3
s = "hello"
print(type(s))
print(s.upper())
print(s.replace("e", "3"))


# 4
class User:
    pass

u = User()
print(u)
print(type(u))

# 5
class User:
    def __init__(self, username, age):
        self.username = username
        self.age = age

u = User("alim", 25)
print(u.username, u.age)


# 6
class Bad:
    items = []

b1 = Bad()
b2 = Bad()
b1.items.append(1)
print(b2.items)


# 7
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.price})"

print(Product("Mouse", 150))
