#!/usr/bin/python 

import threading 
import time

class myThread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		for i in range(1,10):
			print i
		time.sleep(10)
			
if __name__ == '__main__':
	threadTest = myThread()
	threadTest.setDaemon(True)
	threadTest.start()
	## 主线程可以在子线程没有执行结束的时候就退出
	print 'main end...'
