a=1;b=1;count=2
while b<10**999:
    a,b=b,a+b
    count+=1
print(count,a,b)
print(len(str(a)))
print(len(str(b)))