#Q023 Non-abundant sums
# perfect number : sum of its proper divisors is exactly equal to the number
# deficient : if the sum of n's proper divisors is less than n
# abundant : if this sum exceeds n.

import time
start_time = time.time()

def is_abundant(number):
    if number <= 10:
        total=0
        for i in range(1,number):
            if number%i==0:
                total+=i
    else:
        total=1
        loop = number**0.5
        i=2
        while i<=loop:
            if number%i==0:
                total+=i
                if i**2 != number:
                    total+=number//i
            i+=1
    if total > number:
        return True
    return False

abundant_list=[]
for i in range(1,28123):
    if is_abundant(i):
        abundant_list.append(i)

total_list=list(range(1,28123))

for i in abundant_list:
    for j in abundant_list:
        if i+j<28123:
            total_list[i+j-1]=0

print(sum(total_list))
print("calculation time:",time.time()-start_time)
