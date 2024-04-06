from itertools import product 
import string 
import time
import os
os.system ("clear")
print (" \033[92m __  __ ____  _  ___ ")
print (" \033[92m |  \/  | ___|/ |/ _ \ ")
print (" \033[91m | |\/| |___ \| | | | | ")
print (" \033[91m | |  | |___) | | |_| | ")
print (" \033[93m |_|  |_|____/|_|\___/ ")
print ()
print ()
print ()
name = ("\033[94m Welcome to the tool ")
for char in name: 
	print (char,end ="",flush=True)
	time.sleep(0.1)
print ()
print ()
name1 = ("\033[94m Follow me on my Instagram account ahu_orphan ")
for char in name1:
	print (char,end ="",flush=True)
	time.sleep(0.1)
print ()
print ()
min_len = int (input("Enter Your Min len: "))
max_len = int (input("Enter Your Min len: "))
counter = 0
print ()
print ()
print ("\033[92m Please wait, it may take a long time ")
charter = string.ascii_uppercase+string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
file_open = open("WordList.txt","w")
for i in range(min_len,max_len+1):
	for s in product(charter,repeat=i):
		word = "".join(s)
		file_open.write(word)
		file_open.write("\n")
		counter+=1
print ("WordList Genrate As {}".format(counter))

