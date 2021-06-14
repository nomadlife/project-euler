f_cache={0:0, 1:1}
def f(n):
    if (n) not in f_cache:
        f_cache[n] = f(n-1) + f(n-2)
    return f_cache[n]

r_cache={}
def s(n):
    i=1
    while True:
        if (i) not in (r_cache):
            r_cache[i] = sum([int(j) for j in list(str(i))])
        if n == r_cache[i]:
            return i
        i+=1

def s2(n):
    return ((n%9 + 1) * 10**(n//9) -1)%1000000007
    return n%9 * 10**(n//9) + 10**(n//9)-1
    return n%9 * 10**((n+1)//9)

def S(n):
    S=0
    for i in range(1,n+1):
        S+=s2(i)
    return S

# print(s(10))
# print(S(20))

total=0
for i in range(1,41):
    print(i, f(i), S(f(i)))

    # print(i, f(i))
    # print(i, f(i), s2(f(i)))
    # print(i, s2(i))

#     r=S(f(i))%1000000007
#     print(i, f(i), r)
#     total+=r
# print(total%1000000007)

