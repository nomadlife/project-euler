# q014 Longest Collatz sequence
# 11s, atom z8350

def collatz(n):
    if n == 1: 
        return 1
    if (n) not in cache :
        if n%2==0:
            cache[n] = collatz(n/2) +1
        else : 
            cache[n] = collatz(n*3+1) +1
    return cache[n]

cache={}
for i in range(1,1000000):
    collatz(i)

max(cache, key=cache.get)
