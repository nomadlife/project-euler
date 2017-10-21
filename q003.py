# Q003 largest prime factor
# What is the largest prime factor of the number 600851475143 ?

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

number = 600851475143
loop = number**0.5
i=1
while i <= loop:
    if number%i==0:
        number2=number/i
        print(i,number2,end=' ')
        if is_prime(i):
            print(i,"is prime factor")
        elif is_prime(number2):
            print(number2,"is prime factor")
        print("")
    i+=1
