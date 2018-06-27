# Q039 Integer right triangles

results={}
for c in range(5,500):
    for a in range(1,int(c/2*1.414)):
        b = (c**2 - a**2)**0.5
        if b==int(b) and a+b+c<=1000:
            if (a+b+c) in results:
                results[a+b+c]+=1
            else : 
                results[a+b+c]=1
print(results.values())
max(results, key=results.get)