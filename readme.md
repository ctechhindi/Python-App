# Python Programimg Language

Python is high-level programming language, with applications in numerous areas,including web programming, scripting, scientific computing and artificial intelligence.

> Python is processed at runtime by the interpreter, There is no need to compile your program before executing it.

## Version

Python has several different implementations, written in various languages. `CPython`, is the most popular by far.

## Print Statement [Output Text]

```py
print('Hello World')
print  "Hello World"
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

Command-line String Input

```py
print  "Hello"
user_reply =  raw_input("Who goes there?")
print  "You may pass,", user_reply
```

Here is a program to show examples of variables:

```py
a =  123.4
b23 =  'Span'
first_name =  "Jeevan"
b =  432
c = a + b
```

```py
number =  input("Type in a number: ")
text =  raw_input("Type in a String :")
print  "Number is a", type(number)
```

>  `type(variable)` : show variable data type

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

## Python  Casting

Specify a Variable Type

-   int()
-   float()
-   str()

```py
y = int(2.8) # y will be 2
z = float("3") # z will be 3.0
z = str(3.0) # z will be '3.0'
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
n =  input("Number ? ")
if n <  0:
	print  "The absolute valu of", n, "is", -n
else:
	print  "The absolute valu of", n, "is", n
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

## 

```pyDefining Functions

In Python a function is defined using the def keyword:Decisions

### if statement

```py
n =  input("Number ? ")
if n <  0:
	print  "The absolute valu of", n, "is", -n
else:
	print  "The absolute valu of", n, "is", n
```

>  `if, elif, else` : Multi if else statement

## Defining Functions

```py
def  hello():
print  "Hello"

def  area(w, h):
return w * h

def  print_welcome(name):
print  "Welcome", name
```
## Python Collections (Arrays)

There are four collection data types in the Python programming language:

*  `List` is a collection which is ordered and changeable. Allows duplicate members.
*  `Tuple` is a collection which is ordered and unchangeable. Allows duplicate members.
*  `Set` is a collection which is unordered and unindexed. No duplicate members.
*  `Dictionary` is a collection which is unordered, changeable and indexed. No duplicate members.

## Python Lists

A list is a collection which is ordered and changeable. In Python lists are written with square brackets.

``py
thislist = ["apple",an", nt(thislist)
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

### List Length

To determine how many items a list have, use the `len()` method:

```py
thislist = ["apple", "banana", "cherry"]
print(len(thislist)) # Output : 3
```

### List Methods Items

* To add an item to the end of the list, use the `append()` method.
* To add an item at the specified index, use the `insert()` method.
* The `remove()` method removes the specified item.
* The `pop()` method removes the specified index, (or the last item if index is not specified).
* The `del` keyword removes the specified index.
* The `clear()` method empties the list.

  

> The `del` keyword can also delete the list completely

```py
thislist = ["apple", "banana", "cherry"]

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
thiet =, "banana", "cherry"}
print(thisset)
```

**Note:**  Sets are unordered, so the items will appear in a random order.

### Add Items

- To add one item to a set use the  `add()`  method.
- To add more than one item to a set use the  `update()`  method.

 ```py 
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
thisset.update(["orange", "mango", "grapes"])
```

> **Note:** If the item to remove does not exist, `remove()` will raise an error.
> **Note:** If the item to remove does not exist, `discard()` will **NOT** raise an error.

* To determine how many  

>  `Note:` Sets are unordered, so the items will appear in a random order.

### Methods

* To add one items to a set have, use the `lenadd()` method.
* You can also use the `pop()`, method to remove an item, but this method will remove the _last_ item. Remember that sets are unordered, so you will not know what item that gets removed.

**Note:** Sets are _unordered_, so when using the `pop()` method, you will not know which item that gets removed.

* The `clear()` method empties the set.
* The `del` keyword will delete the set completely. ex: `del  thisset`


## Python  Dictionaries

A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.To add more than one item to a set use the `update()` method.

```py
thisdicset =  { 
	"brand": "Ford",  
	"model": "Must{"apple", "bananga",  
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
