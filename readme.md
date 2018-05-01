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
