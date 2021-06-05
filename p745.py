def is_perfect_square(num):
    if num == int(num**0.5)*int(num**0.5):
        return True
    else:
        return False 
    
# def g3(num):
#     if is_perfect_square(num):
#         return num
#     loop = num**0.5
#     res=[]
#     i=2
#     while i < loop:
#         if num%i==0:
#             t=num//i
#             if is_perfect_square(t):
#                 return t
#             res.append(i)
#         i+=1
#     for i in reversed(res):
#         if is_perfect_square(i):
#             return i
#     return 1

def g3(num):
    if is_perfect_square(num):
        return num
    loop = num**0.5
    res=[]
    i=2
    while i < loop:
        if num%i==0:
            t=num//i
            if is_perfect_square(t):
                return t
            res.append(i)
        i+=1
        
    for i in res[::-1]:
        if is_perfect_square(i):
            return i
    return 1

# print(g(75))
n=10**6
tot=0
import time
start=time.time()
for i in range(1, n+1):
    res=g3(i)
#     print(i, res, res2)
    tot+=res
dur = time.time() - start
print(tot, dur)
print(tot%1000000007)