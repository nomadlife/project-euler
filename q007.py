#project-euler q007
#10001st prime number

#####too much slow!!!!!!!!

def prime_check(number):
	i=1;count=0
	while i<=number:
		if number % i == 0:
			count=count+1
		i+=1
	if count==2:
		return True
	else :
		return False

i=1;prime_count=0
while True:
	prime = prime_check(i)
	if prime:
		prime_count+=1
		print("prime nuber ",i,"count :",prime_count)
	if prime_count==10001:
		break
	i+=1
	
