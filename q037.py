# Q037 Truncatable primes, z8350, 16s

from sympy import isprime

total=0;count=0
for i in range(10,1000000):
    if isprime(i):
        string = str(i)
        m = len(string)
        if all(isprime(int(string[:i])) and isprime(int(string[i:])) for i in range(1,m)):
            total+=i
            count+=1
            print(i,total,count)
    if count==11:break
print(total)