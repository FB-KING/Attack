import os,sys
try:
        import os, storage, sys, rich, requests
        mkdir('/sdcard/xxsvr.txt')
        checkhigh = '/sdcard/xxsvr.txt'
        if 'permission denied' in checkhigh:
        	print(f'First Give Storage Permission..');exit()
except ImportError:
        os.system('termux-setup-storage')
        os.system('git pull')
        
def let():
	print('xxxx');exit()
	
	
let()
