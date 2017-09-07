#q010
#Summation of primes
#

# 3,7 번 문제의 소수 확인코드
def isPrime(param):
    if param==1:
        return False
    loop=round(param**0.5)
    for j in range(2,loop+1):
        if param%j == 0:
            return False
        else:
            continue
    return True

# 2000000 까지 소수인지 확인해서 합산 
total =0
for i in range(1,2000000):
    if isPrime(i):
        total += i
		
print(total)
