# Q034 Digit factorials, all, 
import time
start = time.time()

print("expected calculation time : 2 min")

def factorial(num):
    total=1
    while num>1:
        total = total * num
        num-=1
    return total

for i in range(1,10000000):
    total=0
    for j in str(i):
        total += factorial(int(j))
    if total == i:
        print("loop:{} factorial_sum:{} True".format(i,total))

# maximum range proof
for i in range(1,9):
    print("9"*i, factorial(9)*i)


print("Calculation time:",time.time()-start)
