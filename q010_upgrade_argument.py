#q010
#Summation of primes
#
import sys
import time
start_time = time.time()

def is_prime(number):
	loop=round(number**0.5)
	i=2
	while i<=loop:
		if number % i == 0:
			return False
		i+=1
	if number==1:
		return False
	return True

loop=2000000
if len(sys.argv)==2:
    print ("sys.argv==2")
    loop=int(sys.argv[1])
	
i=1;total=0
while i<loop:
	if is_prime(i):
		total=total+i
		print("prime nuber ",i,"sum :",total)
	i+=1

print("start_time", start_time)
print("--- %s seconds ---" %(time.time() - start_time))
