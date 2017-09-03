a=1;b=1;total=0
while True :
    if b>4000000 :
        break
    print(b,end=', ')
    if b%2==0:
        total = total + b
    print(total)
    a,b = b,a+b
