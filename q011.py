# Q011 Largest Product in grid 20x20
# greatest product of four adjacent numbers in the same direction
# (up, down, left, right, or diagonally)

filename = 'q011_data.txt'
with open(filename) as file_object:
	lines = file_object.readlines()

numbers=[]
for line in lines:
	print(line.split())
	numbers.append(line.split())

from functools import reduce

maxValue=0
for i in range(17):
    for j in range(17):
        prod=[]
        prod.append(reduce(lambda x, y: int(x)*int(y), numbers[i][j:j+4]))
        prod.append(reduce(lambda x, y: int(x)*int(y), [numbers[i+k][j] for k in range(0,4)]))
        prod.append(reduce(lambda x, y: int(x)*int(y), [numbers[i+k][j+k] for k in range(0,4)]))
        prod.append(reduce(lambda x, y: int(x)*int(y), [numbers[i+k][j+3-k] for k in range(0,4)]))
        if max(prod) > maxValue:
            maxValue = max(prod)
print(maxValue)
