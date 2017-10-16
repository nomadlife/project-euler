# Q027 Quadratic primes
#Find the product of the coefficients, a and b,
#for the quadratic expression
#that produces the maximum number of primes
#for consecutive values of n, starting with n=0.

import time
start_time = time.time()

def is_prime(num):
    if num<=1:
        return False
    loop=num**0.5
    i=2
    while i<=loop:
        if num%i==0:
            return False
        i+=1
    return True

max_n=0
for a in range(-1000,1001):
    for b in range(-1000,1001):
        n=0
        while True:
            value = n**2 + a*n + b
            if value>0 and is_prime(value):
                n+=1
            else:
                if n>max_n:
                    max_n = n
                    print("a:",a,"b:",b,"new max value n:",n,a*b)
                    break
                else:
                    break

print("calculation time:",time.time() - start_time)
