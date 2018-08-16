fact={'0': 1,
 '1': 1,
 '2': 2,
 '3': 6,
 '4': 24,
 '5': 120,
 '6': 720,
 '7': 5040,
 '8': 40320,
 '9': 362880}

def func(num):
    total=0
    for i in str(num):
        total+=fact[i]
    if (total) in cache:
        return cache[total]
    if total in chain:
        return 
    chain.add(total)
    return func(total)

count=0
cache={}
for i in range(2,1000000):
    chain={i}
    result = func(i)
    if result != None:
        cache[i]=len(chain) + result
    else :
        cache[i]=len(chain)
    if cache[i] ==60:
        count+=1
print('count :',count)