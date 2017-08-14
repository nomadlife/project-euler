#q009
#Special Pythagorean triplet
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

i=1
while i<1000:
	j=1
	while j<=i:
		pythagorean=i**2+j**2
		if pythagorean == (1000-i-j)**2:
			print(i,j,1000-i-j)
			print(i*j*(1000-i-j))
			break
		j+=1
	i+=1
