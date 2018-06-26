# Q035 Circular primes, ~1M, z8350, 25s

from sympy import isprime

count=0
for i in range(2,1000000):
    if isprime(i):
        string = str(i)
        m=len(string)
        if all(isprime(x) for x in [int(string[j:]+string[:j]) for j in range(1,m)]):
            count+=1
print(count)

