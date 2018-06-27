# Q041 Pandigital prime
from sympy import isprime

def getpermutation(string):
    i=len(string)-2
    while i >= 0:
        if string[i] < string[i+1]:
            target = sorted(string[i:])
            new_num = target.pop(target.index(string[i])+1)
            last_nums = ''.join(target)
            return string[:i] + new_num + last_nums
        i-=1
    if i==-1 and len(string)<9:
        return ''.join(sorted(string+str(len(string)+1)))
    return False

i='1'
while i:
    if isprime(i):
        print(i,"is pandigit & prime number")
    i=getpermutation(i)