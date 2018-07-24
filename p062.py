#p062 Cubic permutations, i3,8sec
def isSameDigit(str1,str2):
    if all(str1.count(i) == str2.count(i) for i in str1):
        return True
    return False

target=10000
cubic=[]
index=[0]
for i in range(target):
    value=str(i**3)
    cubic.append(value)
    if i>0 and len(cubic[i]) > len(cubic[i-1]):
        index.append(i)
index.append(target)

for k in range(len(index)-1):
    for i in range(index[k],index[k+1]):
        count=1
        for j in range(i+1,index[k+1]):
            if isSameDigit(cubic[i],cubic[j]):
                count+=1
        if count==5:
            print(i,cubic[i],count)
            break
    else:
        continue
    break