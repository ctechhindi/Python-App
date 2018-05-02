from functions import Functions
root = Functions()

root.info("Output")

print('This message is output to the screen')

print(1,2,3,4)
print(1,2,3,4,sep='-')
print(1,2,3,4,sep='/',end=';')


# Output formatting
root.info("Output formatting")

print('I love {0} and {1}'.format('php','java'))
print('I love {1} and {0}'.format('php','java'))

print('Welcome, {firstname} {lastname}'.format(firstname = 'Jeevan', lastname = 'Lal'))

f = 17.89585252
print('The value of f is %3.2f' %f)
print('The value of f is %3.4f' %f)


# Python Input
root.info("Python Input")

string = input('Enter a value: ')
print("Your Enter Value : ", string)


# Python Import
root.info("Python Import")

import math
import sys

print(math.pi)
print(sys.path)