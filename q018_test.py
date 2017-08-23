#project-euler q018
#Maximum path sum 1
# the 112037th person to have solved this problem.

'''
filename = 'q018_data.txt'
with open(filename) as data:
	lines = data.readlines()
m=len(lines)

numbers=[]
for line in lines:
	print(line.split())
	numbers.append(line.split())
'''

import numpy

filename = 'q018_data.txt'
numbers2=numpy.loadtxt(filename,delimiter='/n',dtype=str)
#print(numbers2)

i=0;numbers3=0
while i<len(numbers2):
	numbers3=(numbers2[i].split())
	i+=1
print(numbers3)


def find_route_down(i,j,total=0,path=''):
	total=total+numbers[i][j]
	path=path+str(numbers[i][j])+";"
	if i==m-1:
		print(total,path)
		return total,path
	else :
		if numbers[i+1][j] < numbers[i+1][j+1]:
			j+=1
	i+=1
	find_route_down(i,j,total,path)

def find_route_up(i,j,total=0,path=''):
	total=total+numbers[i][j]
	path=path+str(numbers[i][j])+";"
	if i==0:
		print(total,path)
		return total,path
	else :
		if numbers[i-1][j] < numbers[i-1][j-1]:
			j-=1
	i-=1
	find_route_up(i,j,total,path)

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

def decision_two_step(i,j):
	return
	
print(biggest_sum())
print(biggest_path())
print(biggest_sum_with_path())
