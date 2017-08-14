#project-euler q014
#Longest Collatz sequence

#the 171451st person to have solved this problem.
#calculation time : 88.9 sec @ 3205U

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
    print("loop :",i,end='')
    chain=collatz(i)
    print(" chain :",chain)
    if chain>max_chain:
        max_chain=chain
        max_i=i
        print("new max_chain :",max_chain,)
    i+=1
print("max_chain :", max_chain,"loop ",max_i)

print("start_time", start_time)
print("--- %s seconds ---" %(time.time() - start_time))
