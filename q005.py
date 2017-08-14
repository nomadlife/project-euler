#project-euler q005
#The smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#LCM

def get_gcd(num1,num2):
	gcd=1
	loop=num1
	if num1>num2:
		loop=num2
	i=1
	while i<=loop:
		if num1%i==0 and num2%i==0:
			gcd =i
		i+=1
	return gcd
	
i=1; gcd=0; lcm=1
while i<20:
	print("loop",i)
	gcd=get_gcd(lcm,i+1)
	print("gcd of",lcm,",",i+1," is :", gcd)
	if gcd==0:
		lcm = lcm*(i+1)
	else:
		lcm = lcm*(i+1)/gcd
	print("lcm",lcm)
	i=i+1

