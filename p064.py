from math import gcd



def reverse(a,b,c,d,n):
    return c,d,a,b,n

def ration(a,b,c,d,n):
    return c*b, abs(d)*b, 0, n-d**2, n

def mini(a,b,c,d,n):
    g=gcd(gcd(a,b),d)
    return int(a/g),int(b/g),c,int(d/g),n

def check(a,b,c,d,n):
    for i in range(int(n**0.5),0,-1):
        temp = (b+i)/d
        if temp == int(temp):
            pop_list.append(int(temp))
            return a,-i,c,d,n
    print("somthing wrong", a,b,c,d,n)
    return a,b,c,d,n

def check_repeat(_list):
    loop = int(len(_list)/2)
    for i in range(2, loop+1):
        if _list[i] == _list[1] and _list[1:i] == _list[i:i+i-1]:
            is_repeat = True
            for j in range(i+i-1, len(_list), i-1):
                if len(_list[1:i]) == len(_list[j:j+i-1]) and _list[j:j+i-1] != _list[1:i]:
                    # print(j, j+i-1, _list[j:j+i-1])
                    is_repeat = False
            if is_repeat:
                # return _list[1:i], len(_list[1:i])
                return len(_list[1:i])
            else:
                continue

count = 0
for j in range(10001):
    if j**0.5 != int(j**0.5):
        pop_list=[]
        frac = (1,0,0,1,j)
        for i in range(1000):
            # print(frac)
            frac = mini(*ration(*reverse(*check(*frac))))
        # print(j, pop_list)
        res = check_repeat(pop_list)
        if res != None and res % 2 != 0:
            count +=1
print(count)

# print(check(1,0,0,1,23))
# print(reverse(1, -4, 0, 1, 23))
# print(ration(0, 1, 1, -4, 23))
# print(mini(1, 4, 0, 7, 23))

# print(ration(0,1,1,-4))
# print(ration(0,7,1,-3))
# print(mini(7, 21, 0, 14))
# print(check(1, 3, 0, 2))
# print(all([2,2,2,2,2]))