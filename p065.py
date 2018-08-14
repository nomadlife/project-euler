def func(i=0):
    if i==target-1:
        return arr[i],1
    else:
        den,num = func(i+1)
        num_n = arr[i]*den + num
        return num_n,den

arr=[2]
for n in range(1,50):
    arr.extend([1,2*n,1])
target=100
nu,de=func()
print(nu,de,nu/de)
print(sum([int(x) for x in str(nu)]))