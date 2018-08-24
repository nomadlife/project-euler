# Q018
#Maximum path sum 1

with open('q018_data.txt') as data:
    numbers = [[int(i) for i in line.split()] for line in data.readlines()]
    
def findSum(i=0,j=0):
    if i==14:
        return numbers[i][j]
    else :
        return numbers[i][j] + max(findSum(i+1,j),findSum(i+1,j+1))
findSum()
