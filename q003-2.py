#project-euler q003
#largest prime factor of the number 600851475143
#half solved(prime check)

def prime_check(number):
	i=1;count=0
	while i<=number:
		if number % i == 0:
			count=count+1
		i=i+1
	return count
	
number=100; i=1
while i<number:
	print("loop :",i)	
	count = prime_check(i)
	print("count is ",count)
	if count == 2:
		#if i is prime number then ckeck if num is divisiable by i or not
		print("This is prime number :",i)
	i = i + 1


