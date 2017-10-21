# q014 Longest Collatz sequence
# Which starting number, under one million, produces the longest chain?

import time
start_time = time.time()

def collatz(num):
    count=1
    while True:
        if num%2==0:
            num=num/2
        elif num==1:
            return count
        else:
            num=num*3+1
        count+=1

i=1;max_chain=0;max_i=0
while i<1000000:
    chain=collatz(i)
    if chain>max_chain:
        max_chain=chain
        max_i=i
        print("loop :",i,"chain :",chain,"max_chain :",max_chain)
    i+=1

print("max_chain :", max_chain,"loop ",max_i)
print("calculation time:",time.time()-start_time)
