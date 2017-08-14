#project-euler q006
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

i=1;total_sq=0;total=0
while i<=100:
	print("loop",i)
	total_sq=total_sq+i**2
	print("total_sq is",total_sq)
	total=total+i
	print("total is ",total)
	i+=1

total=total**2
difference = total_sq - total
print("difference = ",difference)
