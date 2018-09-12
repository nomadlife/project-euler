# q014 Longest Collatz sequence
# 15s, atom z8350

def collatz(num):
    if num == 1: 
        return 1
    elif (num) in cache :
        return cache[num]
    elif num%2==0:
        return collatz(num/2) +1
    else:
        return collatz(num*3+1) +1

cache={}
i=1;maxValue=0
while i < 1000000:
    value = collatz(i)
    if value > maxValue : 
        maxValue = value
    cache[i] = value
    i+=1

print(maxValue)
