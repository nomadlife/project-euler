import time
start_time = time.time()

from time import strftime
now = strftime("%y%m%d-%H%M%S")
import sys
filename ='out-'+sys.argv[0]+'-'+str(now)+'.txt'
orig_stdout = sys.stdout
f = open(filename, 'w')
sys.stdout = f

print(now)
print(sys.argv[0])
#-------------main code from here------------------
i=1;sum=0
while i<500:
	sum=sum+i
	print(i,sum)
	i+=1
#--------------------------------------------
print("start_time", start_time)
print("--- %s seconds ---" %(time.time() - start_time))

sys.stdout = orig_stdout
f.close()
