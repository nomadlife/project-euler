#project-euler q007
#10001st prime number

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

i=1;primeCount=0
while True:
    if isPrime(i):
        primeCount+=1
    if primeCount==10001:
        break
    i+=1
print(i)
