#q010
#Summation of primes
#

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

i=1;total=0
while i<2000000:
	if is_prime(i):
		total=total+i
		print("prime nuber ",i,"sum :",total)
	i+=1

print("start_time", start_time)
print("--- %s seconds ---" %(time.time() - start_time))
