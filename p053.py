# p053 Combinatoric selections
from math import factorial as f

def c(n,r):
    if n == r or r == 0 : 
        return 1
    elif r == 1: 
        return n
    return f(n)/(f(r)*f(n-r))

count =0 
for i in range(1,101):
    for j in range(0,i+1):
        if c(i,j) > 10**6:
            count += 1
print(count)