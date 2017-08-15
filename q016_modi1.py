#project-euler q016
#Power digit sum

# 173982 nd

import time
start_time = time.time()

product=2**1000
print(product)
string=str(product)
total=0
for i in string:
    total=total+int(i)
print(total)

print("start_time", start_time)
print("--- %s seconds ---" %(time.time() - start_time))
