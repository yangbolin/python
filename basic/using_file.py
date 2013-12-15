#!/usr/bin/python 
#Filename:using_file.py 

poem = '''\
programming is fun
When the work is done
if you wanna make your work also fun:
	use Python!
'''

f = file('poem.txt', 'w') # open for writing
f.write(poem)
f.close()

f = file('poem.txt')

while True:
	line = f.readline()
	if len(line) == 0:	#Zero length indcates EOF
		break
	print line, #Notice comma to avoid automatic newline added by python
f.close()
