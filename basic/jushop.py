#!/usr/bin/python
import urllib
import re 
import sys

def main():
	read_file_object = open(sys.argv[1])
	write_file_object = open(sys.argv[2], 'w')
	log = open('jushop.log', 'w')
	pattern = re.compile(r'''<h1(\s*)(.*?)(\s*)title(\s*)=(\s*)([\"\s]*)([^\"\']+?)([\"\s]+)(.*?)>''')
	
	log.write('start grub, please wait in patience...\n')
	try:
		for userid in read_file_object:
			userid = userid.strip('\r\n')
			url = 'http://www.1688.com/company/tb-'+ userid + '.html'
			page = urllib.urlopen(url)
			html = page.read()
			result = pattern.findall(html)
			if result:
				line = url + ' ' +  result[0][6]
				write_file_object.write(line+'\r\n')
			else:
				log.write(userid + ' failed!!!\n')
	finally:
		read_file_object.close()
		write_file_object.close()
	log.write('end grub...\n')
	log.close()
if __name__ == '__main__':
	if len(sys.argv) == 3:
		main()
	else:
		print '#########################################################'
		print '#  please input userid file and output file!!!          #'
		print '#  usage:python jushop.py inputfile.txt outputfile.txt  #'
		print '#########################################################'
