def load_list():
	filename = 'q018_data.txt'
	with open(filename) as data:
		lines = data.readlines()
	global m
	m=len(lines)

	global numbers
	numbers=[]
	for line in lines:
		#print(line.split())
		numbers.append(line.split())

def load_array():
	import numpy

	filename = 'q018_data.txt'
	numbers2=numpy.loadtxt(filename,delimiter='/n',dtype=str)
	#print(numbers2)

	i=0;numbers3=0
	while i<len(numbers2):
		numbers3=(numbers2[i].split())
		i+=1
	print(numbers3)
	#from io import BytesIO
	#numbers4 = numpy.genfromtxt(BytesIO(filename),delimiter=none,dtype=)
	#print(numbers4)
