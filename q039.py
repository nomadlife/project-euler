# Q039 Integer right triangles
result=[0]*1001
for c in range(1,500):
    for a in range(1,int(c/2**0.5)):
        b=(c**2-a**2)**0.5
        if b == int(b) and a+b+c <= 1000:
            result[int(a+b+c)] += 1
print(max(result), result.index(max(result)))