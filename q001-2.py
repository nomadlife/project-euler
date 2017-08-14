sum=0
for num in range(1000) :
	print("loop ",num)
	if num%3==0:
		sum=sum+num
		print(num,", sum =",sum)
	elif num%5==0:
		sum=sum+num
		print(num,", sum =",sum)
	
print(sum)