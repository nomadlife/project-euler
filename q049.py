# Q049 Prime permutations
from sympy import isprime

def cmp_permutation(str1,str2):
    for i in str1:
        if not str1.count(i) == str2.count(i):
            return False
    return True
    
for i in range(1000,10000):
    if isprime(i):
        for j in range(i+3330,10000,3330):
            if isprime(j) and cmp_permutation(str(i),str(j)):
                print(i,j)