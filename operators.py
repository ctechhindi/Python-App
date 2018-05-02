from functions import Functions
root = Functions()

# Arithmetic operators
root.info("Arithmetic operators")
x = 25
y = 7

print('x + y =',x+y)
print('x - y =',x-y)
print('x * y =',x*y)
print('x / y =',x/y)
print('x // y =',x//y)
print('x ** y =',x**y)


# Comparison operators
root.info("Comparison operators")
a = 15
b = 20

print('a > b  is',a>b)
print('a < b  is',a<b)
print('a == b is',a==b)
print('a != b is',a!=b)
print('a >= b is',a>=b)
print('a <= b is',a<=b)

# Identity operators
root.info("Identity operators")
x1 = 2
y1 = 2
x2 = 'Python'
y2 = 'Python'
x3 = [1,2,3]
y3 = [1,2,3]

print(x1 is not y1)
print(x2 is y2)
print(x3 is y3)


# Membership operators
root.info("Membership operators")
x = 'Python App'
y = {1:'x',2:'y'}

print('P' in x)
print('app' not in x)
print(1 in y)
print('a' in y)