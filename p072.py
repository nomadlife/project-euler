print("hello")

def reduced(a,b):
    i=a
    while i >= 2:
        if b%i==0 and a%i==0:
            b = b / i
            a = a / i
            break
        else:
            i-=1
    return int(a),int(b)


cache=set()
target=1000
import time
start = time.time()

for i in range(2,target+1):
    for j in range(1,i):
        # res = reduced(j,i)
        # print(j,i, res)
        if (j,i) not in cache:
            cache.add(reduced(j,i))

dur = time.time() - start
print("target : ", target)
print("answer : ", len(cache))
print("time : ", dur)