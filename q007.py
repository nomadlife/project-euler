# Q007
#10001st prime number

def is_prime(num):
    if num==1:
        return False
    loop=num**0.5
    i=2
    while i<=loop:
        if num%i==0:
            return False
        i+=1
    return True

i=1;primeCount=0
while True:
    if is_prime(i):
        primeCount+=1
    if primeCount==10001:
        break
    i+=1
print(i)
