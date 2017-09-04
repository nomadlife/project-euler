#project-euler q007
#10001st prime number

def prime_check(number):
	if number==1:
		return False
	loop=round(number**0.5)
	i=2
	while i<=loop:
		if number % i == 0:
			return False
		i+=1
	return True

i=1;prime_count=0
while True:
	prime = prime_check(i)
	if prime:
		prime_count+=1
		print("prime nuber ",i,"count :",prime_count)
	if prime_count==10001:
		break
	i+=1
