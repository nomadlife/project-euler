print("P-072")
import time
import math 

def reduced(a,b):
    i=a
    while i >= 2:
        if b%i==0 and a%i==0:
            b = b / i
            a = a / i
            break
        else:
            i-=1
    return a,b

def reduced2(a,b):
    gcd = math.gcd(a,b)
    return a/gcd, b/gcd

cache=set()
target=17

start = time.time()

for i in range(2,target+1):
    for j in range(1,i):
        # res = reduced(j,i)
        # print(j,i, res)
        # if (j,i) not in cache:
        cache.add(reduced2(j,i))

for i in range(2,target+1):
    for j in range(1,i):
        cache.add(reduced2(j,i))

dur = time.time() - start
print("target : ", target)
print("answer : ", len(cache))
# print(cache)
print("time : ", dur)