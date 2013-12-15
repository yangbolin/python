#!/usr/bin/python

import urllib
import re 
import sys
import threading
import socket

class jushop(threading.Thread):
	def __init__(self, readFile, writeFile, logFile):
		threading.Thread.__init__(self)	 	
		self.read_file = readFile		
		self.write_file = writeFile		
		self.log_file = logFile

	def run(self):
		print 'reading ' + self.read_file + ' start...'
		read_file_object = open(self.read_file)			## read userid from this file
		write_file_object = open(self.write_file, 'w')	## write grub data to this file
		log = open(self.log_file, 'w')						## write grub log to this file
		## the regex to grub specified label
		pattern = re.compile(r'''<h1(\s*)(.*?)(\s*)title(\s*)=(\s*)([\"\s]*)([^\"\']+?)([\"\s]+)(.*?)>''')
	
		log.write('start grub, please wait in patience...\n')
		try:
			for userid in read_file_object:
				userid = userid.strip('\r\n')
				log.write(userid + ' start...\n')
				url = 'http://www.1688.com/company/tb-'+ userid + '.html'
				try:
					page = urllib.urlopen(url)
					html = page.read()
				except:
					log.write(userid + ' exception...\n')
					continue
				
				result = pattern.findall(html)
				if result:
					line = url + ' ' +  result[0][6]
					write_file_object.write(line+'\r\n')
				else:
					log.write(userid + ' failed!!!\n')
				log.write(userid + ' end...\n')
		finally:
			read_file_object.close()
			write_file_object.close()
		log.write('end grub...\n')
		log.close()
		
		print 'reading ' + self.read_file + ' end...'

if __name__ == '__main__':
	socket.setdefaulttimeout(60)	## socket timeout
	## start a new thread for every small file
	thread00 = jushop('jushop_00', 'qingguo_00.txt', 'jushop_00.log')
	thread00.start()
	thread01 = jushop('jushop_01', 'qingguo_01.txt', 'jushop_01.log')
	thread01.start()
	thread02 = jushop('jushop_02', 'qingguo_02.txt', 'jushop_02.log')
	thread02.start()
	thread03 = jushop('jushop_03', 'qingguo_03.txt', 'jushop_03.log')
	thread03.start()
	thread04 = jushop('jushop_04', 'qingguo_04.txt', 'jushop_04.log')
	thread04.start()
	thread05 = jushop('jushop_05', 'qingguo_05.txt', 'jushop_05.log')
	thread05.start()
	thread06 = jushop('jushop_06', 'qingguo_06.txt', 'jushop_06.log')
	thread06.start()
	thread07 = jushop('jushop_07', 'qingguo_07.txt', 'jushop_07.log')
	thread07.start()
	thread08 = jushop('jushop_08', 'qingguo_08.txt', 'jushop_08.log')
	thread08.start()
	thread09 = jushop('jushop_09', 'qingguo_09.txt', 'jushop_09.log')
	thread09.start()
	thread10 = jushop('jushop_10', 'qingguo_10.txt', 'jushop_10.log')
	thread10.start()
	thread11 = jushop('jushop_11', 'qingguo_11.txt', 'jushop_11.log')
	thread11.start()
	thread12 = jushop('jushop_12', 'qingguo_12.txt', 'jushop_12.log')
	thread12.start()
