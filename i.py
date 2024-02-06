import os,sys
try:
        import os, storage, sys, rich, requests
        mkdir('/sdcard/xxsvr.txt')
except ImportError:
        os.system('termux-setup-storage')
        os.system('git pull')
        checkhigh = '/sdcard/xxsvr.txt'
        if 'permission denied' in checkhigh:
        	print(f'First Give Storage Permission..');exit()
def let():
	print('xxxx');exit()
	
	
let()
