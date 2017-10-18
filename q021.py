# Q021

def getSumOfDivisors(number):
    total=0
    for i in range(1,number):
        if number%i==0:
            total=total+i
    return(total)

grandTotal=0
grandTotalList=[]
for i in range(1,10001):
    result_a = getSumOfDivisors(i)
    result_b = getSumOfDivisors(result_a)
    if i == result_b and i != result_a:
        print(i,result_a,"are Amicable number")
        if i not in grandTotalList:
            grandTotal = grandTotal + i
            grandTotalList.append(i)
        if result_a not in grandTotalList:
            grandTotal = grandTotal + result_a
            grandTotalList.append(result_a)

print(grandTotal)
print(grandTotalList)
