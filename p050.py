# p050 Consecutive prime sum
from sympy import isprime

primes=[ i for i in range(1,5000) if isprime(i)]
results={}
for i in range(len(primes)):
    for j in range(i+1,len(primes)):
        summ=sum(primes[i:j])
        if summ>1000000:
            break
        if isprime(summ):
            results[i,j-i]=summ
			
max(results.items(), key=lambda k: k[0][1])