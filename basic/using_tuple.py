#!/usr/bin/python
#FileName:using_tuple.py 

zoo = ('wolf', 'elephant', 'pengui')
print 'Number of animals in the zoo is', len(zoo)		#output 3

new_zoo = ('monkey', 'dolphin', zoo)	
print 'Number of animals in the new zoo is', len(new_zoo)	#output 3, the third elem is still a tuple
print 'All animals in new zoo are', new_zoo	#output	('monkey', 'dolphin', ('wolf', 'elephant', 'pengui'))
print 'Animals brought from old zoo are', new_zoo[2]	#output ('wolf', 'elephant', 'pengui')
print 'Last animal brought form old zoo is', new_zoo[2][2]	#pengui
