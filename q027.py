# Q027 Quadratic primes
#Find the product of the coefficients, a and b,


import time
start_time = time.time()
from sympy import isprime

max_n=0
for a in range(-1000,1001):
    for b in range(-1000,1001):
        n=0
        while True:
            value = n**2 + a*n + b
            if value>0 and isprime(value):
                n+=1
            else:
                if n>max_n:
                    max_n = n
                    print("a:",a,"b:",b,"new max value n:",n,a*b)
                    break
                else:
                    break

print("calculation time:",time.time() - start_time)
