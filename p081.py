# p081 Path sum: two ways
with open('p081_matrix.txt') as data:
    number = [[int(i) for i in line.split(',')] for line in data.readlines()]

size=80
for i in range(size):
    for j in range(size):
        if i==0 and j==0:
            pass
        elif i==0:
            number[i][j] = number[i][j] + number[i][j-1]
        elif j==0:
            number[i][j] = number[i][j] + number[i-1][j]
        else:
            number[i][j] = number[i][j] + min(number[i-1][j],number[i][j-1])

print(number[size-1][size-1])