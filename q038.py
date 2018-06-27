# Q038 Pandigital multiples
maxvalue=[]
for i in range(1,10000):
    n='';j=1
    while len(n)<9:
        n=n+str(i*j)
        j+=1
        if len(n)==9:
            if all(i in n for i in '123456789'):
                maxvalue.append(n)
print(max(maxvalue))