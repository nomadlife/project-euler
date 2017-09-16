def factorial(number):
    total=1
    for i in range(number,1,-1):
        total=total*i
    return total

number='0123456789'
target=1000000
value=0
for i in range(10):
    value=factorial(9-i)
    count=0
    while value<=target:
        target=target-value
        count+=1
    number = number[:i]+number[i+count]+number[i:i+count]+number[i+count+1:]
print(number)
print(target)

#final value is millio+1th value. 