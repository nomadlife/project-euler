# check prime. speed up by square root.
def isprime(n):
    if n == 0 or n==1:
        return False
    i=2
    loop=n**0.5
    while i <= loop:
        if n%i == 0:
            return False
        i+=1
    return True

# replace and check if prime
def rep(num, s):
    text = str(num)
    if s not in text:
        return False
    cnt = text.count(s)

    # result list
    res=[]

    # replace and check if prime
    for i in range(int(s), 10):
        test = text.replace(s, str(i), cnt)
        if isprime(int(test)):
            res.append(test)

    return res, len(res)


for i in range(100, 10000000):
    # target replacing number should start with 0,1,2. from 3, impossible to get 8 list.
    for s in '012':
        res = rep(i, s)

        # print out
        if res:
            if res[1] > 6:
                print(i, s, res)

