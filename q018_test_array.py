#project-euler q018
#

import time
start_time = time.time()

import numpy

filename = 'q018_data.txt'
with open(filename) as file_object:
	lines = file_object.readlines()



'''
for line in lines:
	print(len(line))
'''

m = len(lines)
n = len(lines[m-1])
numbers = numpy.zeros((m,n))

i = 0
while i < m:
	j = 0
	while j<len(lines[i])/3:
		#print(lines[i][j*3]+lines[i][j*3+1],end='')
		numbers[i][j]=lines[i][j*3]+lines[i][j*3+1]
		print('{:2} '.format(int(numbers[i][j])),end='')
		j += 1
	print("")
	i += 1

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

def find_biggest(i=0,j=0,path=''):
	if i==m-1:
		string=str(number[i][j]
		return numbers[i][j],string
	else :
		num1,path1=biggest_route(i+1,j,path)
		num2,path2=biggest_route(i+1,j+1,path)
		if num1>num2:
			string=str(num1)
			return numbers[i][j]+num1,string
		else :
			string=str(num2)
			return numbers[i][j]+num2,string

def biggest_route(i=0,j=0):
	if i==m-1:
		return str(numbers[i][j])
	else :
		num1=biggest_route(i+1,j)
		num2=biggest_route(i+1,j+1)
		if num1>num2:
			return str(numbers[i][j])+str(num1)
		else :
			return str(numbers[i][j])+str(num2)

def biggest_sum(i=0,j=0):
	if i==m-1:
		return numbers[i][j]
	else :
		num1=biggest_sum(i+1,j)
		num2=biggest_sum(i+1,j+1)
		if num1>num2:
			return numbers[i][j]+num1
		else :
			return numbers[i][j]+num2

def decision_two_step(i,j):
	return

def test_return_two_value():
	a=1;b='test'
	return a,b

print(test_return_two_value())
'''
print("numbers[0][0]",numbers[0][0])
print(find_route_down(0,0))
print("numbers[14][7]",numbers[14][7])
print(find_route_up(14,7))
#print("numbers[7][3]",numbers[7][3])
#print(find_route_down(7,3))
#print("numbers[7][3]",numbers[7][3])
#print(find_route_up(7,3))
print(biggest_sum())
print(biggest_route())
'''






'''
import numpy
a=numpy.empty((10,10))
a.fill(foo)
print(a)


import numpy as np
twoD = np.array([[]*m]*n)
twoD = np.array([[x]*m]*n)


myList=[]
for i in range(10):
	myList.append(1)
	print(myList[i],len(myList))
print(myList)
'''

print("start_time", start_time)
print("--- %s seconds ---" %(time.time() - start_time))
