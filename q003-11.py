#project-euler q003
#largest prime factor of the number 600851475143

#other's solution

factor, max_prime = 2, 0
number = 600851475143
while 1:
	if (number%factor == 0):
		number = number/factor
		if factor>max_prime:
			max_prime = factor
		if number == 1:
			break
	else:
		factor+=1

print "\n\t---------------------------------------------------------"
print "\t|\tEl maximo primo de", 600851475143," es: ", max_prime, "\t|"
print "\t---------------------------------------------------------\n"
