# p092 , 172s, atom, z8350
cache={}
for i in range(1,10000000):
    number=i
    while True:
        if number == 1 or number == 89:
            cache[i]=number
            break
        summ=0
        while number>0:
            summ+=(number%10)**2
            number//=10
        number=summ
        if (number) in cache:
            cache[i]=cache[number]
            break
print(sum(value == 89 for value in cache.values()))