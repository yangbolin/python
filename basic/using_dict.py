#!/usr/bin/python
#FileName:using_dict.py 

# 'ab' is short for address book

ab = { 'Swaroop':'Swaroop@alibaba-inc.com',
	   'Larry':'larry@alibaba-inc.com',
	   'Matsumoto':'matz@alibaba-inc.com',
	   'Spammer':'spammer@alibaba-inc.com'
	}

print "Swaroop's address is %s" %ab['Swaroop']

#Adding a key/value pair
ab['Guido'] = 'guio@alibaba-inc.com'
#Deleting a key/value pair 
del ab['Spammer']

print '\nThere are %d contacts in the address-book\n'%len(ab)

for name, address in ab.items():	
	print 'Contact %s at %s'%(name, address)
if 'Guido' in ab:#OR ab.has_key('Guido')
	print "\nGuido's address is %s" %ab['Guido']
