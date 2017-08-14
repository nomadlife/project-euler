#project-euler q012
#Highly divisible triangular number

# 166554th person to have solved this problem.
import time
start_time = time.time()

def factor_count(number):
	i=2;count=1
	loop=number**0.5
	while i<loop:
		if number%i==0:
			count+=1
		i+=1
	return count

i=1;sum=0
while i<1000:
	sum=sum+i
	count=factor_count(sum)
	print(i,sum,count)
	i+=1

print("start_time", start_time)
print("--- %s seconds ---" %(time.time() - start_time))
