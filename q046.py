# p046 Goldbach's other conjecture
from sympy import isprime

def is_goldbach_conjecture(num):
    for i in range(2,num):
        if isprime(i):
            j=1
            while True:
                total = i + 2 * j**2
                if total == num:
                    return True
                elif total > num :
                    break
                j+=1
                
for i in range(2,10000):
    if not i%2 == 0 and not isprime(i):
        if is_goldbach_conjecture(i):
            continue
        else:
            print(i,"is not goldbach")
            break
