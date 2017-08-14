import sys
orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f

import time
start_time = time.time()

i=1;sum=0
while i<100:
	sum=sum+i
	#print(i,sum)
	i+=1

print(sum)
print(time.time())
print("start_time", start_time)
print("--- %s seconds ---" %(time.time() - start_time))


sys.stdout = orig_stdout
f.close()
