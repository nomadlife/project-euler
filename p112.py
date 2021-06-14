print("P112")

def isbouncy(num):
    text = str(num)
    inc = True
    for k,v in enumerate(text):
        if k==0:
            continue
        if text[k-1] <= v:
            continue
        else:
            inc = False
    dec = True
    for k,v in enumerate(text):
        if k==0:
            continue
        if text[k-1] >= v:
            continue
        else:
            dec = False
    if inc or dec:
        return False
    else:
        return True

# print(isbouncy(134468))
# print(isbouncy(66420))
# print(isbouncy(155349))

cnt = 0
cntb = 0
for i in range(1,10000000):
    res = isbouncy(i)
    if res:
        cntb += 1
    cnt += 1
    if cntb/cnt*100 >= 99:
        print(i, cntb/cnt*100)
        break