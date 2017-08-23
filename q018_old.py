


#numbers = [int(i) for i in numbers] # only for string not list
#numbers = list(map(int, numbers)) # not possible

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
'''


'''
def test_return_two_value():
	a=1;b=2;c='test';d=21
	return a,str(b)+c,str(a)+str(b)+str(d)
print(test_return_two_value())

print("numbers[0][0]",numbers[0][0])
print(find_route_down(0,0))
print("numbers[14][7]",numbers[14][7])
print(find_route_up(14,7))
#print("numbers[7][3]",numbers[7][3])
#print(find_route_down(7,3))
#print("numbers[7][3]",numbers[7][3])
#print(find_route_up(7,3))

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
