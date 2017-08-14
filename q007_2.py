#project-euler q007
#10001st prime number

#####little bit faster,,, but stil slow !!!!

def prime_check(number):
	i=2
	if number==1:
		return False
	while i<number:
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
	
