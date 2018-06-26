# q014 Longest Collatz sequence
# Which starting number, under one million, produces the longest chain?

import time
start_time = time.time()

def collatz(num):
    if num == 1: 
        return 1
    elif (num) in cache :
        return cache[num]
    elif num%2==0:
        return collatz(num/2) +1
    else:
        return collatz(num*3+1) +1

cache={}
i=1;maxValue=0
while i < 1000000:
    value = collatz(i)
    if value > maxValue : 
        maxValue = value
    cache[i] = value
    i+=1

print("max_chain :", max_chain,"loop ",max_i)
print("calculation time:",time.time()-start_time)
