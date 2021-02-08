#Ispisivanje serijskog broja u terminalu
import subprocess
import os
import time



result = subprocess.run(['sudo' , 'st-info', '--probe' ],stdout= subprocess.PIPE) #pomocu toga u terminalu ispisujem serijski broj st linka 
#list1=subprocess.Popen("pgrep -u root", stdout= subprocess.PIPE, shell = True)

#Samo za debug
#print(result.stdout)

Y = str(result.stdout)
index=0
new_list=[]
while index < len(Y):
	index = Y.find(' serial:', index)   
	if index == -1:      
		break
	new_list.append((str(Y[index+13:index+37])))
	index+=2
	
print(new_list)

