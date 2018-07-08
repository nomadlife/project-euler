# p058 Spiral primes 13s, z8350
from sympy import isprime

i=3;count=1;countPrime=0
while True:
    num=i**2
    for j in range(1,4):
        num-=(i-1)
        if isprime(num):
            countPrime+=1
        count+=1
    count+=1
    if countPrime/count<0.1:
        break
    i+=2