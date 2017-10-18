a=1;b=1;count=1
while a<10**999:
    a,b=b,a+b
    count+=1
print(count,a)
print(len(str(a)))
