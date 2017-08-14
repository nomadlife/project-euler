i=1;sum=0
while i<1000 :
	print("loop ",i)
	if i%3==0:
		sum=sum+i
		print(i,", sum =",sum)
	elif i%5==0:
		sum=sum+i
		print(i,", sum =",sum)
	i=i+1

print(sum)
