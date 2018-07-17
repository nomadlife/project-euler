from math import gcd

def phi(num):
    count=1
    for i in range(2,num):
        if gcd(num,i)==1:
            count+=1
    return count

prime=[2,3,5,7,11,13,17,19]
number=1
for n in prime:
    number*=n
    if number<1000000:
        v=phi(number)
        print(n,number,v,number/v)