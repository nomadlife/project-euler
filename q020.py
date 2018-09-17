# Q020 Factorial digit sum

def fact(num):
    total=1
    for i in range(1,num+1):
        total*=i
    return total

total=0
string=str(fact(100))
for i in string:
    total+=+int(i)
total
