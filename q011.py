# Q011 Largest Product in grid 20x20
# greatest product of four adjacent numbers in the same direction

with open('q011_data.txt') as f:
	numbers = [[int(j) for j in i.split()] for i in f.readlines()]

def prod(arr):
    total =1
    for i in arr:
        total *= i
    return total

result=[]
for i in range(20):
    for j in range(20):
        result.append(max(\
            prod(numbers[i][j:j+4]),
            prod([numbers[i+k][j] for k in range(min(20-i,4))]),
            prod([numbers[i+k][j+k] for k in range(min(20-i,20-j,4))]),
            prod([numbers[i+k][j+3-k] for k in range(min(20-i,20-j-3,4))])))
max(result)
