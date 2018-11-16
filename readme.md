# Python Programimg Language

Python is high-level programming language, with applications in numerous areas,including web programming, scripting, scientific computing and artificial intelligence.

> Python is processed at runtime by the interpreter, There is no need to compile your program before executing it.

[GitHub](https://github.com/jeevan15498/Python-App)

[IPython](https://ipython.org/install.html)

## Version : 3.x

Python has several different implementations, written in various languages. `CPython`, is the most popular by far.

## Print Statement [Output Text]

```py
print('Hello World')
print  "Hello World"
```

The actual syntax of the print() function is :

`print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)`


```py
print(1,2,3,4, sep='/', end=';')
# Output: 1/2/3/4;
```

Output formatting

```py
print('I love {0} and {1}'.format('php','java'))
# Output: I love php and java

print('Welcome, {firstname} {lastname}'.format(firstname = 'Jeevan', lastname = 'Lal'))
# Output: Welcome, Jeevan Lal

f = 17.89585252
print('The value of f is %3.2f' %f)
# Output: The value of f is 17.90

print('The value of f is %3.4f' %f)
# Output: The value of f is 17.8959
```

## Operations

Python has the capability of carrying out calculations.

```css
>>> 2 + 2
4
>>> 5 + 4 - 3
6
>>> 2 * (3 + 4)
14
>>> 10 / 2
5.0 # return float
>>> 5 ** 2 # Power (Exponentiation)
25
```

> Using a single slash to divide numbers produces a decimal (or `float`, as it is called in programming). We'll have more about floats in a letter lesson.

Dividing by zero in Python produces an error, as no answer can be calculated.

```css
>>> 11 / 0
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

## Input and Variables

Here is a program to show examples of variables:

```py
a =  123.4
b23 =  'Span'
first_name =  "Jeevan"
b =  432
c = a + b
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

Command-line String Input

```py
number =  input("Type in a number: ")
text =  raw_input("Type in a String :")
print  "Number is a", type(number)
```

>  `type(variable)` : Show variable data type

Here is the list of some string operations:

| Operation | Symbol | Example |
| --------- | ------ | ------- |
| Repertition | * | "i" * 5 == "iiiii" |
| Concatenation | + | "Hello, " + "World" == "Hello, World" |

## Python  NumbersThere are three numeric types in Python:

-   int
-   float
-   complex

```py
x = 1  # int  
y = 2.8  # float  
z = 1j # complex
```
> To verify the type of any object in Python, use the `type()` function

- `Float` can also be scientific numbers with an "e" to indicate the power of 10. ex : `y = 35e3`
- `Complex` numbers are written with a "j" as the imaginary part. ex ; `y = 5j`

## Python Casting

Conversion between data types

```py
int(10.6) # Output : 10
int(-10.6) # Output : -10
float(5) # Output : 5.0
float('2.5') # Output : 2.5
str(25) # Output : '25'
set([1,2,3]) # Output : {1, 2, 3}
tuple({5,6,7}) # Output : (5, 6, 7)
list('hello') # Output : ['h', 'e', 'l', 'l', 'o']
dict([[1,2],[3,4]]) # Output : {1: 2, 3: 4}
dict([(3,26),(4,44)]) # Output : {3: 26, 4: 44}
```

## Python  Strings

String literals in python are surrounded by either single quotation marks, or double quotation marks.

`'hello'`  is the same as  `"hello"`.

### Methods

- Get the character at position

```py
a = "Hello, World!"  
print(a[1]) # Output : e
print(b[2:5]) # Output : llo
```
- The `strip()` method removes any whitespace from the beginning or the end.
- The `len()` method returns the length of a string.
- The `lower()` method returns the string in lower case.
- The `upper()` method returns the string in upper case.
- The `replace()` method replaces a string with another string.
- The `split()` method splits the string into substrings if it finds instances of the separator

```py
a = " Hello, World! "  
print(a.strip()) # returns "Hello, World!"
print(len(a))
print(a.lower())
print(a.upper())
print(a.replace("H", "J"))
print(a.split(",")) # returns ['Hello', ' World!']
```
## Python  Operators

### Python Comparison Operators

Comparison operators are used to compare two values:
```py
==	,Equal,	x == y	
!=	,Not equal,	x != y	
>	,Greater than,	x > y	
<	,Less than,	x < y	
>=	,Greater than or equal to,	x >= y	
<=	,Less than or equal to,	x <= y
```

### Python Logical Operators

Logical operators are used to combine conditional statements:

```py
and ,Returns True if both statements are true,	x < 5 and  x < 10	
or  ,Returns True if one of the statements is true,	x < 5 or x < 4	
not ,Reverse the result, returns False if the result is true, not(x < 5 and x < 10)
```

### Python Identity Operators

Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

```py
is 	,Returns true if both variables are the same object,	x is y	
is not	,Returns true if both variables are not the same object,	x is not y
```

### Python Membership Operators

Membership operators are used to test if a sequence is presented in an object:

```py
in 	,Returns True if a sequence with the specified value is present in the object,	x in y	
not in	,Returns True if a sequence with the specified value is not present in the object,	x not in y
```

## Decisions

### if statement

```py
n = input("Number ?")
if n <  0:
    print "The absolute valu of", n, "is", -n
else:
    print "The absolute valu of", n, "is", n
```

>  `if, elif, else` : Multi if else statement

#### Short Hand If

If you have only one statement to execute, you can put it on the same line as the if statement.

```py
if a > b: print("a is greater than b")
```
#### Short Hand If ... Else

One line if else statement

```py
print("A") if a > b else  print("B")
```

One line if else statement, with 3 conditions

```py
print("A") if a > b else  print("=") if a == b else  print("B")
```

## Python Functions

```py
def hello():
    print "Hello"

def area(w, h):
    return w * h

def print_welcome(name):
    print "Welcome", name
```
## Python Collections (Arrays)

There are four collection data types in the Python programming language:

*  `List` is a collection which is ordered and changeable. Allows duplicate members.
*  `Tuple` is a collection which is ordered and unchangeable. Allows duplicate members.
*  `Set` is a collection which is unordered and unindexed. No duplicate members.
*  `Dictionary` is a collection which is unordered, changeable and indexed. No duplicate members.

## Python Lists

A list is a collection which is ordered and changeable. In Python lists are written with square brackets.

```py
thislist = ["apple", "banana", "cherry"]
print(thislist[1]) # Access Items
thislist[1] =  "blackcurrant"  # Change Item Value
```
### Loop Through a List

You can loop through the list items by using a `for` loop:

```py
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
```

Output :

```
apple
banana
cherry
```

### Check if Item Exists

```py
thislist = ["apple", "banana", "cherry"]
if  "apple"  in thislist:
    print("Yes, 'apple' is in the fruits list")
```

### Methods

* To add an item to the end of the list, use the `append()` method.
* To add an item at the specified index, use the `insert()` method.
* The `remove()` method removes the specified item.
* The `pop()` method removes the specified index, (or the last item if index is not specified).
* The `del` keyword removes the specified index.
* The `clear()` method empties the list.
* To determine how many items a list have, use the `len()` method.


> The `del` keyword can also delete the list completely

```py
thislist = ["apple", "banana", "cherry"]

print(len(thislist)) # Output : 3
thislist.append("orange")
thislist.insert(1, "orange")
del thislist[0]
del thislist # The del keyword can also delete the list completely
thislist.clear()
print(thislist)
```

## Python Tuples

A tuple is a collection which is ordered and `unchangeable`. In Python tuples are written with round brackets.

```py
thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(thistuple[1]) # Access Tuple Items
```

* Once a tuple is created, you cannot change its values. Tuples are `unchangeable`.
* Tuples are `unchangeable`, so you cannot `remove` items from it, but you can delete the tuple completely.


## Python Sets

A set is a collection which is `unordered` and `unindexed`. In Python sets are written with curly brackets.

```py
thisset = {"apple", "banana", "cherry"}
print(thisset)
```

**Note:** Sets are unordered, so the items will appear in a random order.

### Add Items

- To add one item to a set use the  `add()`  method.
- To add more than one item to a set use the  `update()`  method.

```py 
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
thisset.update(["orange", "mango", "grapes"])
```

### Remove Item

To remove an item in a set, use the `remove()`, or the `discard()` method.

> **Note:** If the item to remove does not exist, `remove()` will raise an error.

> **Note:** If the item to remove does not exist, `discard()` will **NOT** raise an error.

* To determine how many

>  `Note:` Sets are unordered, so the items will appear in a random order.

### Methods

* To determine how many items a set have, use the `len()` method.
* You can also use the `pop()`, method to remove an item, but this method will remove the _last_ item. Remember that sets are unordered, so you will not know what item that gets removed.

**Note:** Sets are _unordered_, so when using the `pop()` method, you will not know which item that gets removed.

* The `clear()` method empties the set.
* The `del` keyword will delete the set completely. ex: `del  thisset`


## Python  Dictionaries

A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

```py
thisdict =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
```

### Accessing Items 

```py
x = thisdict["model"]
# There is also a method called `get()` that will give you the same result
x = thisdict.get("model")
```

### Loop Through a Dictionary

You can also use the `values()` function to return values of a dictionary

```py
for x in thisdict.values():  
    print(x)
```

Loop through both _keys_ and _values_, by using the `items()` function.

```py
for x, y in thisdict.items():  
    print(x, y)
```

### Methods

* `Check if Key Exists`
 : To determine if a specified key is present in a dictionary use the `in` keyword.
* `Length` : To determine how many items (key-value pairs) a dictionary have, use the `len()` method.
* `Removing Items` : The `pop()` method removes the item with the specified key name.
* The `del` keyword removes the item with the specified key name.
* The `clear()` keyword empties the dictionary. ex : `thisdict.clear()`

## Python Loops

Python has two primitive loop commands:

* `while` loops
* `for` loops

### The while Loop

```py
i = 1
while i < 6:
    print(i)
    i += 1
```

> **Note**: remember to increment i, or else the loop will continue forever.

### Methods

* With the `break` statement we can stop the loop even if the while condition is true.
* With the `continue` statement we can stop the current iteration, and continue with the next.

### For Loops

A `for` loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

```py
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
```

Even strings are iterable objects, they contain a sequence of characters

```py
for x in "banana":
    print(x)
```

## The range() Function

To loop through a set of code a specified number of times, we can use the `range()` function,

The `range()` function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

```py
for x in range(6):
    print(x)
```

> Note that `range(6)` is not the values of 0 to 6, but the values 0 to 5.

The `range()` function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: `range(2, 30, 3)`

## Python Classes and Objects

* Create a class named MyClass, with a property named x.
* Now we can use the class named myClass to create objects.

```py
class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)
```

### The __init__() Function

* To understand the meaning of classes we have to understand the built-in __init__() function.
* All classes have a function called __init__(), which is always executed when the class is being initiated.

```py
# Create a class named Person, use the __init__() function to assign values for name and age:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
```

> `Note:` The __init__() function is called automatically every time the class is being used to create a new object.

Insert a function that prints a greeting, and execute it on the p1 object:

```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
```

> `Note`: The `self` parameter is a reference to the class instance itself, and is used to access variables that belongs to the class.

### Methods

* `Modify Object Properties:` p1.age = 40
* `Delete Object Properties:` del p1.age
* `Delete Objects:` del p1

## Python Iterators

## Python Import

A module is a file containing Python definitions and statements. Python modules have a filename and end with the extension `.py`

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

## Python Modules

* Consider a module to be the same as a code library.
* A file containing a set of functions you want to include in your application.

### Create a Module

To create a module just save the code you want in a file with the file extension `.py`:

```py
# Save this code in a file named mymodule.py
def greeting(name):
    print("Hello, " + name)
```

### Use a Module

Now we can use the module we just created, by using the `import` statement:


```py
import mymodule

mymodule.greeting("Jonathan")
```

> `Note`: When using a function from a module, use the syntax: `module_name.function_name`.

### Variables in Module

Save this code in the file `mymodule.py`

```py
person1 = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}
```

```py
import mymodule

a = mymodule.person1["age"]
print(a)
```

### Re-naming a Module

You can create an alias when you import a module, by using the `as` keyword:

```py
import mymodule as mx

a = mx.person1["age"]
print(a)
```

### Built-in Modules

```py
import platform

print(platform.system())
```

### Using the `dir()` Function

There is a built-in function to list all the function names (or variable names) in a module. The `dir()` function:

```py
import platform

x = dir(platform)
print(x)
```

> `Note`: The `dir()` function can be used on all modules, also the ones you create yourself.

### Import From Module

You can choose to import only parts from a module, by using the from keyword.


```py
# The module named `mymodule` has one function and one dictionary:
def greeting(name):
    print("Hello, " + name)

person1 = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}
```

```py
# Import only the person1 dictionary from the module:
from mymodule import person1

print (person1["age"])
```

## Python Datetime

A date in Python is not a data type of its own, but we can import a module named `datetime` to work with dates as date objects.

```py
import datetime

x = datetime.datetime.now() # 2018-11-16 12:11:11.644662
print(x)
print(x.year)
print(x.strftime("%A"))
```

### Creating Date Objects

```py
import datetime

x = datetime.datetime(2020, 5, 17)
print(x)
```

A reference of all the legal format codes: [DateTime](https://www.w3schools.com/python/python_datetime.asp)

## Python JSON

Python has a built-in package called `json`, which can be use to work with JSON data.

### Parse JSON - Convert from JSON to Python

If you have a JSON string, you can parse it by using the `json.loads()` method.

```py
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
```

### Convert from Python to JSON

If you have a Python object, you can convert it into a JSON string by using the `json.dumps()` method.

```py
import json

# a Python object (dict):
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
```

You can convert Python objects of the following types, into JSON strings:

```py
import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
```

### Format the Result

The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.

The `json.dumps()` method has parameters to make it easier to read the result:

```py
# You can also define the separators, default value is (", ", ": ")
json.dumps(x, indent=4, separators=(". ", " = "))
```

### Order the Result

Use the sort_keys parameter to specify if the result should be sorted or not:

```py
json.dumps(x, indent=4, sort_keys=True)
```

## Python PIP

PIP is a package manager for Python packages, or modules if you like.

> **Note:** If you have Python version 3.4 or later, PIP is included by default.

### What is a Package?
A package contains all the files you need for a module.

Modules are Python code libraries you can include in your project.

### Check if PIP is Installed

```shell
$ pip --version
```

### Install PIP

If you do not have PIP installed, you can download and install it from this page: [https://pypi.org/project/pip/](https://pypi.org/project/pip/)

### Download a Package

```shell
$ pip install camelcase
```

### Using a Package

Once the package is installed, it is ready to use.

```py
import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))
```

### Find Packages
Find more packages at https://pypi.org/.

### Remove a Package
Use the uninstall command to `remove` a package:

```shell
$ pip uninstall camelcase
```

### List Packages

Use the `list` command to list all the packages installed on your system:

```shell
$ pip list
```

## Python Try Except

* The `try` block lets you test a block of code for errors.
* The `except` block lets you handle the error.
* The `finally` block lets you execute code, regardless of the result of the try- and except blocks.

```py
# The try block will generate an exception, because x is not defined:
try:
  print(x)
except:
  print("An exception occurred")
```

### Finally

The `finally` block, if specified, will be executed regardless if the try block raises an error or not.


```py
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
```

This can be useful to close objects and clean up resources:

```py
# Try to open and write to a file that is not writable:
try:
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()
```