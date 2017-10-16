# q012 Highly divisible triangular number

import time
start_time = time.time()

def count_factors(num):
    loop=num**0.5
    # for square number
    if loop==int(loop):
        count=1
    else:
        count=0
    i=1
    while i<loop:
        if num%i==0:
            count+=2
        i+=1
    return count

i=1;tri_num=0
while True:
    tri_num = tri_num + i
    count = count_factors(tri_num)
    print("loop:",i,"tri_num",tri_num,"count",count)
    if count > 500:
        break
    i+=1

print("answer:",tri_num)
print("calculation time:",time.time()-start_time)
