# Q048 Self powers
total = 0
for i in range(1,1001):
    total += pow(i,i)
print(str(total)[-10:])