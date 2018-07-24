#p067 Maximum path sum II
# 100 rows
with open('p067_triangle.txt') as data:
    numbers = [[int(i) for i in line.split()] for line in data.readlines()]

def findSum(i=0,j=0):
    if (i, j) in cache:
        return cache[i,j]
    if i == 99:
        cache[i,j] = numbers[i][j]
    else :
        cache[i,j] = max(findSum(i+1,j),findSum(i+1,j+1)) + numbers[i][j]
    return cache[i, j]
cache={}
findSum()