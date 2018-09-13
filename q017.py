# Q017 Number letter counts

data1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
       30,40,50,60,70,80,90,100,1000]
data2='''one two three four five six seven eight nine ten 
eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen
twenty thirty forty fifty sixty seventy eighty ninety hundred thousand'''
numbers=dict(zip(data1,data2.split()))

def func(n):
    if n <100:
        if (n) not in numbers:
            numbers[n] = numbers[n-n%10] + numbers[n%10]
        return numbers[n]
    if n <1000:
        if n%100==0:
            return  numbers[n//100] +  numbers[100]
        return numbers[n//100] +  numbers[100] + 'and' + numbers[n%100]
    return 'one' + numbers[1000]

total=0
for i in range(1,1001):
    total+=len(func(i))
print(total)
