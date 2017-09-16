def isAbundant(number):
    total=0
    if number > 10:
        i=2
        loop = number**0.5
        total+=1
        while i<=loop:
            if number%i==0:
                total+=i
                if i != number/i:
                    total+=number//i
            i+=1
    else:
        i=1
        while i<number:
            if number%i==0:
                #print(i,end=';')
                total+=i
            i+=1
    return total>number

abundant_list=[]
for i in range(1,28123):
    if isAbundant(i):
        abundant_list.append(i)

total_list=list(range(1,28123))
for i in abundant_list:
    for j in abundant_list:
        if i+j<28123:
            total_list[i+j-1]=0

print(sum(total_list))