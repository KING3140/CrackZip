import os
import zipfile
import sys
from time import sleep
os.system('clear')
print('''

 ______     ______     ______     ______     __  __     ______     __     ______  
/\  ___\   /\  == \   /\  __ \   /\  ___\   /\ \/ /    /\___  \   /\ \   /\  == \ 
\ \ \____  \ \  __<   \ \  __ \  \ \ \____  \ \  _"-.  \/_/  /__  \ \ \  \ \  _-/ 
 \ \_____\  \ \_\ \_\  \ \_\ \_\  \ \_____\  \ \_\ \_\   /\_____\  \ \_\  \ \_\   
  \/_____/   \/_/ /_/   \/_/\/_/   \/_____/   \/_/\/_/   \/_____/   \/_/   \/_/   
                                                                                  


Author    ===>> king
Instagram ===>> @the.empiresec
GitHub    ===>> https://github.com/theEmpireSec
\n
''')
if len(sys.argv)!=3:
	print(''' Usage option > python3 crackZip.py <path of zipfile> <path of dictionary>''')
	sys.exit()
def crack():
	zip_file=sys.argv[1]
	wordlist=sys.argv[2]
	wordlist=open(wordlist,'r',encoding="ISO-8859-1")
	zip_file=zipfile.ZipFile(zip_file)
	for word in wordlist:
		try:
			zip_file.extractall(pwd=word.strip())
			print('[+] Password found ===>>> '+word,'\n[+] File extracted ')
			sys.exit()
		except:
			pass
crack()
