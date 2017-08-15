#project-euler q003
#largest prime factor of the number 600851475143
#solved 

num = 600851475143
test_num = round(num**0.5)
prime=False
prime_factor=0

def factor_check(numerator,denominator):
	if numerator%denominator==0:
		return True
	else :
		return False

def prime_check(number):
	i=1;count=0
	while i<=number:
		if number % i == 0:
			count=count+1
		i=i+1
	if count==2:
		return True
	else :
		return False

i=1
while i<test_num:
	factor=factor_check(num,i)
	if factor:
		prime = prime_check(i)
		if prime:
			print("*This is prime factor :",i)
			prime_factor=i
	i=i+1
	
print(prime_factor)
