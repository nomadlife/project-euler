# Q018
#Maximum path sum 1

with open('q018_data.txt') as data:
    numbers = [[i for i in line.split()] for line in data.readlines()]
	
def findSum(i=0,j=0):
    if i==14:
        return int(numbers[i][j])
    else :
        result1 = findSum(i+1,j)
        result2 = findSum(i+1,j+1)
        if result1>result2:
            return int(numbers[i][j])+result1
        else:
            return int(numbers[i][j])+result2

findSum()
