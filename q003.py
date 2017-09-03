#project-euler q003
#largest prime factor of the number 600851475143
#solved

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

number = 600851475143
loopSize = round(number**0.5)
for i in range(1,loopSize+1):
    if number%i==0:
        number2=number/i
        print(i,number2,end=' ')
        if isPrime(i):
            print(i,"is prime factor")
        elif isPrime(number2):
            print(number2,"is prime factor")
        print("")
