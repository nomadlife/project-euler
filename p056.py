# p056 Powerful digit sum
maxsum = 0
for i in range(1,101):
    for j in range(1,101):
        number=pow(i,j)
        digitsum=sum([int(x) for x in str(number)])
        if digitsum>maxsum:
            maxsum=digitsum
print(maxsum)