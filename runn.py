import os

import sys

 

f=open("Counter.txt")
b=f.read()
print("Running the script : ", sys.argv[1], "....\n")
#print(os.getcwd())
b=int(b)
for x in range(0,100):
	os.system('python3 ' + sys.argv[1]+ '> '+str(b)+'.txt')
	b+=1
f.close()
f=open("Counter.txt", "w")
f.write(str(b))
f.close()	
os.system('python3 stats_maker.py') 

 
