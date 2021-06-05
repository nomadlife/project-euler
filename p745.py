from math import sqrt

def is_perfect_square(num):
    if num == int(num**0.5)*int(num**0.5):
        return True
    else:
        return False 

def is_perfect_square2(num):
    if num == int(num**0.5)**2:
        return True
    else:
        return False 

def is_perfect_square3(num):
    temp = num**0.5
    if temp == int(temp):
        return True
    else:
        return False 

def is_perfect_square4(num):
    temp = sqrt(num)
    if temp == int(temp):
        return True
    else:
        return False 

isps={}
def is_perfect_square5(num):
    if (num) in isps:
        return isps[num]
    else:
        temp = num**0.5
        if temp == int(temp):
            isps[num]=True
            return True
        else:
            isps[num]=False
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

def g4(num):
    if is_perfect_square3(num):
        return num
    loop = num**0.5
    res=[]
    i=2
    while i < loop:
        if num%i==0:
            t=num//i
            if is_perfect_square3(t):
                return t
            res.append(i)
        i+=1
        
    for i in res[::-1]:
        if is_perfect_square3(i):
            return i
    return 1

def g5(num):
    if is_perfect_square5(num):
        return num
    loop = num**0.5
    res=[]
    i=2
    while i < loop:
        if num%i==0:
            t=num//i
            if is_perfect_square5(t):
                return t
            res.append(i)
        i+=1
    
    for j in range(len(res)-1,-1,-1):
        if is_perfect_square5(res[j]):
            return res[j]
    return 1


# print(g(75))
n=10**6
tot=0
import time
start=time.time()

# for i in range(1, n+1):
#     res=g5(i)
#     # print(i, res)
#     tot+=res

# mem={}
# for i in range(1, n+1):
#     t=i**2
#     if t <= n:
#         j=t
#         while j <= n :
#             mem[j]=t
#             j+=t
# tot = sum(mem.values())

mem={}
loop=n**0.5
for i in range(1, int(loop)+1):
    t=i**2
    j=t
    while j <= n :
        # if (j) not in mem:
        mem[j]=t
        j+=t
tot = sum(mem.values())


# mem={}
# loop=n**0.5
# for i in range(int(loop), 0, -1):
#     t=i**2
#     j=t
#     while j <= n :
#         if (j) not in mem:
#             mem[j]=t
#         j+=t
# tot = sum(mem.values())


dur = time.time() - start
print(tot, dur)
print(tot%1000000007)