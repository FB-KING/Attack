import os,sys
try:
	import os, sys, rich, requests
	try:
		mkdir('/sdcard/xxsvr.txt')
	except:print('sex');exit()
	checkhigh = '/sdcard/xxsvr.txt'
	if 'permission denied' in checkhigh:
		print(f'First Give Storage Permission..');exit()
except PermissionError:
	os.system('termux-setup-storage')
	#os.system('termux-setup-storage')
      #  os.system('git pull')
	
def let():
	print('xxxx');exit()
	
	
let()
