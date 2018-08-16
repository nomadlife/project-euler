# Q029 Distinct powers

mylist=[]
for a in range(2,101):
    print(a,end=',')
    for b in range(2,101):
        value=pow(a,b)
        if mylist.count(value) ==0:
            mylist.append(value)
print()
print("answer:",len(mylist))
