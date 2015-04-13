#!/usr/bin/python
# @author 	boris.yangbl
# @comment 	fast commit code use svn
# @date		2015-04-13

import os
import sys

# switch work dir
directory = raw_input('please enter absolute directory path : ')
os.chdir(directory)
print 'current directory is ' + os.getcwd()

# svn up 
is_up = raw_input('please enter Y to execute svn up : ')
if is_up == 'Y':
	print '#####################svn up########################'
	output = os.popen('svn up')
	up_log = output.read();
	print up_log
	print '###################################################'
	# resolve conflict
	has_conflict = False
	up_log_lines = up_log.split('\n')
	for up_log_line in up_log_lines:
		up_log_line_arr = up_log_line.split('\t\t')
		if 'C' == up_log_line_arr[0]:
			print 'conflicts exist in ' + up_log_line_arr[1]
			has_conflict = True
	if has_conflict == True:
		print 'conflict exists in your local, please resolve it...'
		sys.exit()

# show code modify
output = os.popen('svn st')
modify_log = output.read()
print '###############current code modify as follows#################'
print modify_log
print '##############################################################'

# confirm modify
raw_input('please enter any key to confirm your modification.......')
modify_log_lines = modify_log.split('\n')

# svn del && svn add
for modify_log_line in modify_log_lines:
	modify_log_line_arr = modify_log_line.split('       ')
	if '!' == modify_log_line_arr[0]:
		output = os.popen('svn del ' + modify_log_line_arr[1])
		print output.read()
	elif '?' == modify_log_line_arr[0]:
		output = os.popen('svn add ' + modify_log_line_arr[1])
		print output.read()

# show log
output = os.popen('svn st')
print '#########################pre commit message####################'
print output.read()
print '###############################################################'

# confirm to commit
choice = raw_input('please enter Y to commit or N to quit.......')
if 'Y' == choice:
	commit_message = raw_input('please enter commit message[blank not contained] : ')
	output = os.popen('svn ci -m ' + commit_message)
	print '##################commit result#######################'
	print output.read()
	print '######################################################'
elif 'N' == choice:
	print '#######################quit###########################'
	print 'please commit by yourself......'
	print '######################################################'
	sys.exit()
print 'Done...Thanks for using...best wishes to you ^=^'
