#project-euler q003
#largest prime factor of the number 600851475143
#solved. short code

num = 600851475143
test_num = round(num**0.5)
prime_factor=0

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
	if num%i==0:
		if prime_check(i):
			print("*This is prime factor :",i)
			prime_factor=i
	i=i+1
	
print(prime_factor)
