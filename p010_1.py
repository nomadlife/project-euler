# q010
# Summation of primes
# add user input

import sys
import time
start_time = time.time()


def is_prime(num):
    if num == 1:
        return False
    loop = num**0.5
    i = 2
    while i <= loop:
        if num % i == 0:
            return False
        i += 1
    return True


loop = 2000000
if len(sys.argv) == 2:
    print("sys.argv==2")
    loop = int(sys.argv[1])

i = 1
total = 0
while i < loop:
    if is_prime(i):
        total = total+i
        print("prime nuber ", i, "sum :", total)
    i += 1

print("time : ",time.time() - start_time)
