from math import gcd
basis=2/5
for i in range(1000000,1,-1):
    value=int(i*3/7)
    if value/i < 3/7 and value/i > basis:
        basis=value/i
        print(value,i,gcd(value,i))