from functions import Functions
root = Functions()

# Create Python Function
root.info("Create Python Function")

def demo(name):
    # passed parameter
    print("Hello, " + name + ". Good morning!")


# How to call a function in python?
root.info("How to call a function in python?")

demo("Jeevan")

# The return statement
root.info("The return statement")
def absolute_value(num):
	if num >= 0:
		return num
	else:
		return -num

print(absolute_value(5))
print(absolute_value(-10))


# Python Default Arguments
root.info("Python Default Arguments")
def demo_fuc(name, msg = "Good morning!"):
   print("Hello",name + ', ' + msg)

demo_fuc("Jeevan")
demo_fuc("Tinku","How do you do?")