#project-euler q012
#Highly divisible triangular number

# 166554th person to have solved this problem.
import time
start_time = time.time()

from time import strftime
now = strftime("%y%m%d-%H%M%S")
import sys
filename ='out-'+sys.argv[0]+'-'+str(now)+'.txt'
orig_stdout = sys.stdout
f = open(filename, 'w')
sys.stdout = f

print(now)
print(sys.argv[0])

def factor_count(number):
	i=2;count=1
	loop=number**0.5
	while i<loop:
		if number%i==0:
			count+=1
		i+=1
	return count

i=1;t_number=0
while True:
	print("loop :",i,end='')
	t_number=t_number+i
	print(" t_number :",t_number,end='')
	count=factor_count(t_number)
	print(" half number of factors :",count)
	if count > 250:
		break
	i+=1

print(t_number)
print("--- %s seconds ---" %(time.time() - start_time))

sys.stdout = orig_stdout
f.close()
