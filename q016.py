#project-euler q016
#Power digit sum

# 173982 nd

import time
start_time = time.time()

product=2**1000
print(product)
loop=str(product)
print(len(loop))
print(loop[0])
print(loop[1])
print(int(loop[0])+int(loop[1]))
loop_len=len(loop)
i=0;total=0
while i<loop_len:
    print("loop:",i)
    total=total+int(loop[i])
    print(total)
    i+=1

print(total)

print("start_time", start_time)
print("--- %s seconds ---" %(time.time() - start_time))
