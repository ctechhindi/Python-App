from functions import Functions
root = Functions()

# Variable in Python
a = 18
b = "Google.com"; c = 45.90
d = {1:'value','key':2}

# Assigning multiple values to multiple variables
root.info("Assigning multiple values to multiple variables")
a, b, c = 5, 3.2, "Hello"
print(a, b, c)

# Multi-line statement
a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9

print("Multi-line statement Value : ", a)

# Data types in Python
root.info("Data types in Python")
print(a, "is of type", type(a))
print(b, "is of type", type(b))
print(c, "is of type", type(c))
print(d, "is of type", type(d))

# Conversion between data types
root.info("Conversion between data types")
float(5)
int(10.6)
int(-10.6)
str(25)
set([1,2,3])
tuple({5,6,7})
list('hello')
dict([[1,2],[3,4]])
dict([(3,26),(4,44)])