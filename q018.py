# Q018
#Maximum path sum 1

filename = 'q018_data.txt'
with open(filename) as data:
	lines = data.readlines()
m=len(lines)

numbers=[]
for line in lines:
	print(line.split())
	numbers.append(line.split())

def biggest_sum_with_path(i=0,j=0):
	# not completed
	if i==m-1:
		return numbers[i][j],numbers[i][j]
	else :
		num1,str1=biggest_sum_with_path(i+1,j)
		num2,str2=biggest_sum_with_path(i+1,j+1)
		if num1>num2:
			return int(numbers[i][j])+int(num1),numbers[i][j]+","+str1
		else :
			return int(numbers[i][j])+int(num2),numbers[i][j]+","+str2

def biggest_path(i=0,j=0):
	if i==m-1:
		return numbers[i][j]
	else :
		num1=biggest_path(i+1,j)
		num2=biggest_path(i+1,j+1)
		if num1>num2:
			return numbers[i][j]+","+num1
		else :
			return numbers[i][j]+","+num2

def biggest_sum(i=0,j=0):
	if i==m-1:
		return numbers[i][j]
	else :
		num1=biggest_sum(i+1,j)
		num2=biggest_sum(i+1,j+1)
		if num1>num2:
			return int(numbers[i][j])+int(num1)
		else :
			return int(numbers[i][j])+int(num2)

print(biggest_sum())
#print(biggest_path())
#print(biggest_sum_with_path())
