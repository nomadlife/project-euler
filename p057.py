# p057 Square root convergents
n=3;d=2;loop=0;count=0
while loop<1000:
    if len(str(n)) > len(str(d)):
        count+=1
    n,d = n+2*d,n+d
    loop+=1
print(count)