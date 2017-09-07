#q009
#Special Pythagorean triplet
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

for i in range(1,1000):
    for j in range(1,i):
        if i**2 + j**2 == (1000-i-j)**2 and i+j < 1000:
            print(i,j,1000-i-j)
            print(i*j*(1000-i-j))
            break
