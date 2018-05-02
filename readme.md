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