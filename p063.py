#p063 Powerful digit counts
count=0
for p in range(1,22):
    for n in range(1,10):
        val=pow(n,p)
        if len(str(val))==p:
            count+=1
print(count)