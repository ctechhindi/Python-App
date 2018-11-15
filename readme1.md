# Python App
[GitHub](https://github.com/jeevan15498/Python-App)

[IPython](https://ipython.org/install.html)

## Requirements

- Using Python 3.6.5

# Doc

## Variable\DataType in Python

```py
a = 18
b = "Google.com"; c = 45.90
d = {1:'value','key':2}
```

__Assigning multiple values to multiple variables__
```py
a, b, c = 5, 3.2, "Hello"
print(a, b, c)
```

__Multi-line statement__
```py
a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9
```

### Data types in Python
```py
print(a, "is of type", type(a))
print(b, "is of type", type(b))
print(c, "is of type", type(c))
print("d is of type", type(d))

# Output
# 45 is of type <class 'int'>
# 3.2 is of type <class 'float'>
# Hello is of type <class 'str'>
# {1: 'value', 'key': 2} is of type <class 'dict'>
```

__Conversion between data types__

```py
float(5) # Output : 5.0
float('2.5') # Output : 2.5
int(10.6) # Output : 10
int(-10.6) # Output : -10
str(25) # Output : '25'
set([1,2,3]) # Output : {1, 2, 3}
tuple({5,6,7}) # Output : (5, 6, 7)
list('hello') # Output : ['h', 'e', 'l', 'l', 'o']
dict([[1,2],[3,4]]) # Output : {1: 2, 3: 4}
dict([(3,26),(4,44)]) # Output : {3: 26, 4: 44}
```
---


## Python Input, Output and Import

```py
print('This message is output to the screen')

# Output: This message is output to the screen
```

The actual syntax of the print() function is

```
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

```py
print(1,2,3,4)
# Output: 1 2 3 4

print(1,2,3,4,sep='-')
# Output: 1-2-3-4

print(1,2,3,4,sep='/',end=';')
# Output: 1/2/3/4;
```


### Output formatting

```py
print('I love {0} and {1}'.format('php','java'))
# Output: I love php and java

print('I love {1} and {0}'.format('php','java'))
# Output: I love java and php

print('Welcome, {firstname} {lastname}'.format(firstname = 'Jeevan', lastname = 'Lal'))
# Output: Welcome, Jeevan Lal

f = 17.89585252
print('The value of f is %3.2f' %f)
# Output: The value of f is 17.90

print('The value of f is %3.4f' %f)
# Output: The value of f is 17.8959
```


### Python Input

```py
string = input('Enter a value: ')
# Output: Enter a value: __ENTER VALUE__

print(Your Enter Value : string)
# Output: Your Enter Value : __ENTER VALUE__
```

### Python Import

A module is a file containing Python definitions and statements. Python modules have a filename and end with the extension .py.

```py
import math
import sys

print(math.pi)
print(sys.path)

# Output: 3.141592653589793
# Output:
['',
 'C:\\Users\\G.one\\AppData\\Local\\Programs\\Python\\Python36-32\\Scripts\\ipython.exe',
 'c:\\users\\g.one\\appdata\\local\\programs\\python\\python36-32\\python36.zip',
 'c:\\users\\g.one\\appdata\\local\\programs\\python\\python36-32\\DLLs',
 'c:\\users\\g.one\\appdata\\local\\programs\\python\\python36-32\\lib',
 'c:\\users\\g.one\\appdata\\local\\programs\\python\\python36-32',
 'C:\\Users\\G.one\\.ipython'
]
```
---

## Python Operators

### Arithmetic operators

| Operator | Meaning |
| -------- | ------- |
| + | Add two operands or unary plus |
| - | Subtract right operand from the left or unary minus |
| * | Multiply two operands |
| / | Divide left operand by the right one (always results into float)	 |
| % | Modulus - remainder of the division of left operand by the right |
| // | Floor division - division that results into whole number adjusted to the left in the number line |
| ** | Exponent - left operand raised to the power of right |

```py
x = 25
y = 7

print('x + y =',x+y)
# Output: x + y = 32

print('x - y =',x-y)
# Output: x - y = 18

print('x * y =',x*y)
# Output: x * y = 175

print('x / y =',x/y)
# Output: x / y = 3.5714285714285716

print('x // y =',x//y)
# Output: x // y = 3

print('x ** y =',x**y)
# Output: x ** y = 6103515625
```

### Comparison operators

| Operator | Meaning |
| -------- | ------- |
| > | Greater that - True if left operand is greater than the right |
| < | Less that - True if left operand is less than the right |
| == | Equal to - True if both operands are equal |
| !- | Not equal to - True if operands are not equal |
| >= | Greater than or equal to - True if left operand is greater than or equal to the right |
| <= | Less than or equal to - True if left operand is less than or equal to the right |


```py
a = 15
b = 20

print('a > b  is',a>b)
# Output: a > b is False

print('a < b  is',a<b)
# Output: a < b is True

print('a == b is',a==b)
# Output: a == b is False

print('a != b is',a!=b)
# Output: a != b is True

print('a >= b is',a>=b)
# Output: a >= b is False

print('a <= b is',a<=b)
# Output: a <= b is True
```

### Logical operators

| Operator | Meaning |
| -------- | ------- |
| and | True if both the operands are true |
| or | True if either of the operands is true |
| not | True if operand is false (complements the operand) |


### Bitwise operators

Bitwise operators act on operands as if they were string of binary digits. It operates bit by bit, hence the name.

### Assignment operators

| Operator | Example | Equivatent to |
| -------- | ------- | ------------- |
| += | x += 2 | x = x + 2 |
| -= | x -= 2 | x = x - 2 |

and more..

### Special operators

> Identity operators

| Operator | Meaning |
| -------- | ------- |
| is | True if the operands are identical (refer to the same object) |
| is not | True if the operands are not identical (do not refer to the same object) |

```py
x1 = 2
y1 = 2
x2 = 'Python'
y2 = 'Python'
x3 = [1,2,3]
y3 = [1,2,3]

print(x1 is not y1)
# Output: False

print(x2 is y2)
# Output: True

print(x3 is y3)
# Output: False
```


> Membership operators

| Operator | Meaning |
| -------- | ------- |
| in | True if value/variable is found in the sequence |
| not in | True if value/variable is not found in the sequence |

```py
x = 'Python App'
y = {1:'x',2:'y'}

print('P' in x)
# Output: True

print('app' not in x)
# Output: True

print(1 in y)
# Output: True

print('a' in y)
# Output: False
```
---

## Python if...else Statement

Syntax

```
if test expression:
    statement(s)
```

Syntax

```
if test expression:
    Body of if
else:
    Body of else
```

Syntax

```
if test expression:
    Body of if
elif test expression:
    Body of elif
else: 
    Body of else
```
---

## Python for Loop

Syntax

```
for val in sequence:
	Body of for
```

```py
# List of numbers
numbers = [7, 4, 8, 2]

# variable to store the sum
sum = 0

# iterate over the list
for val in numbers:
	sum = sum+val

print("The sum is", sum)
# Output: The sum is 21
```

### The range() function

We can generate a sequence of numbers using range() function. range(10) will generate numbers from 0 to 9 (10 numbers).

We can also define the start, stop and step size as `range(start,stop,step size)`. step size defaults to 1 if not provided.

```py
print(range(10))
# Output: range(0, 10)

print(list(range(10)))
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(range(2, 8)))
# Output: [2, 3, 4, 5, 6, 7]

print(list(range(2, 20, 3)))	
# Output: [2, 5, 8, 11, 14, 17]
```

```py
fruits = ['Apple', 'Mango', 'Orange']

# iterate over the list using index
for i in range(len(fruits)):
	print("I like", fruits[i])

# Output :
I like Apple
I like Mango
I like Orange
```

### for loop with else

```py
digits = [a, b, c]

for i in digits:
    print(i)
else:
    print("No items left.")

# Output :
a
b
c
No items left.
```

---

## Python while Loop

Syntax

```
while test_expression:
    Body of while
```


```py
# Program to add natural
# numbers upto 
# sum = 1+2+3+...+n

n = 10
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

print("The sum is", sum)
# Output : The sum is 55
```

### while loop with else

```py
counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")

# Output :
Inside loop
Inside loop
Inside loop
Inside else
```

---

## Python break and continue

### Python break statement

Syntax

```
break
```

```py
# Use of break statement inside loop

for val in "string":
    if val == "i":
        break
    print(val)

print("The end")

# Output :
s
t
r
The end
```

### Python continue statement

Syntax

```
continue
```

```py
# Program to show the use of continue statement inside loops

for val in "string":
    if val == "i":
        continue
    print(val)

print("The end")

# Output :
s
t
r
n
g
The end
```

---

## Python pass statement

In Python programming, pass is a null statement

Syntax 

```
pass
```

```py
# pass is just a placeholder for
# functionality to be added later.
sequence = {'p', 'a', 's', 's'}
for val in sequence:
    pass
```

We can do the same thing in an empty function or class as well.

```py
def function(args):
    pass
```

```py
class example:
    pass
```
---

## Python Functions

### Types of Functions

1. `Built-in functions` - Functions that are built into Python.
2. `User-defined functions` - Functions defined by the users themselves.

Syntax

```
def function_name(parameters):
    """docstring"""
    statement(s)
```

Above shown is a function definition which consists of following components.

1. Keyword `def` marks the start of function header.
2. A function name to uniquely identify it. Function naming follows the same rules of writing identifiers in Python.
3. Parameters (arguments) through which we pass values to a function. They are optional.
4. A colon `(:)` to mark the end of function header.
5. Optional documentation string (docstring) to describe what the function does.
6. One or more valid python statements that make up the function body. Statements must have same indentation level (usually 4 spaces).
7. An optional `return` statement to return a value from the function.

```py
def demo(name):
    # passed parameter
    print("Hello, " + name + ". Good morning!")
```

#### How to call a function in python?

```py
demo('Jeevan')

# Output :
Hello, Jeevan. Good morning!
``` 

### The return statement

The return statement is used to exit a function and go back to the place from where it was called.

Syntax

```
return [expression_list]
```

```py
print(greet("May"))

# Output :
Hello, May. Good morning!
None
```

Here, None is the returned value.

```py
def absolute_value(num):
    if num >= 0:
        return num
    else:
        return -num

print(absolute_value(5))
# Output: 5

print(absolute_value(-10))
# Output: 10
```

### How Function works in Python?

![DEMO](https://cdn.programiz.com/sites/tutorial2program/files/python-how-function-works_1.jpg)


### Scope and Lifetime of variables

```py
def demo_function():
    x = 23
    print("Value inside function:",x)

x = 56
demo_function()
print("Value outside function:",x)

# Output :
Value inside function: 23
Value outside function: 56
```

### Python Function Arguments

#### Python Default Arguments

We can provide a default value to an argument by using the assignment operator (=). Here is an example.

```py
def greet(name, msg = "Good morning!"):
   print("Hello",name + ', ' + msg)

greet("Jeevan")
greet("Tinku","How do you do?")

# Output :

Hello Jeevan, Good morning!
Hello Tinku, How do you do?
```

#### Python Keyword Arguments

When we call a function with some values, these values get assigned to the arguments according to their position.

```py
# 2 keyword arguments
greet(name = "Bruce",msg = "How do you do?")

# 2 keyword arguments (out of order)
greet(msg = "How do you do?",name = "Bruce") 

# 1 positional, 1 keyword argument
greet("Bruce",msg = "How do you do?")         
```

#### Python Arbitrary Arguments

In the function definition we use an asterisk (*) before the parameter name to denote this kind of argument. Here is an example.

```py
def greet(*names):
   # names is a tuple with arguments
   for name in names:
       print("Hello",name)

greet("Ram","Raj","Adesh")

# Output :

Hello Ram
Hello Raj
Hello Adesh
```
