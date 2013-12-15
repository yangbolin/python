#!/usr/bin/python 
# FileName:func_doc.py 

def printMax(x,y):
	'''Prints the maximum of two numbers.
	
	The two values must be integers.'''
	
	x = int(x) #convert to integers, if possible
	y = int(y)
	
	if x > y:
		print x, 'is maximum'
	else:
		print y, 'is maximum'

printMax(3, 5)

# print the docstring of printMax 
print printMax.__doc__

# print function printMax,which is an object in python 
print printMax
