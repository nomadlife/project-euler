#project-euler q017
#Number letter counts

# the 116033rd person to have solved this problem.
import numpy
import time
start_time = time.time()

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
	while j<len(lines[i]):
		#print(lines[i][j*3]+lines[i][j*3+1],end='')
		numbers[i][j]=lines[i][j]+lines[i][j+1]
		print('{:2d} '.format(int(numbers[i][j])),end='')
		j += 3
	print("")
	i += 1







'''
import numpy
a=numpy.empty((10,10))
a.fill(foo)
print(a)
'''

'''
import numpy as np
twoD = np.array([[]*m]*n)
twoD = np.array([[x]*m]*n)
'''

'''
myList=[]
for i in range(10):
	myList.append(1)
	print(myList[i],len(myList))
print(myList)
'''

print("start_time", start_time)
print("--- %s seconds ---" %(time.time() - start_time))
