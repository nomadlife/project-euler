from decimal import *

decimalSize=2000
getcontext().prec = decimalSize
maxLength=[0,0]
for d in range(1,1000):
    string=str(Decimal(1)/Decimal(d))
    string=string[string.find(".")+1:]
    cycleString='';exit1=False
    for idx,val in enumerate(string):
        end=int(string.find(val,idx+1))
        while end != -1 and end<decimalSize*0.5:
            length=end-idx
            test=string[idx:end]
            test2=string[end:end+length]
            if test==test2 and string.count(test)*length > decimalSize*0.9:
                cycleString=test
                end=-1
                exit1=True
            else :
                end=int(string.find(val,end+1))
        if exit1:break
    if len(cycleString)>maxLength[1]:
        maxLength=d,len(cycleString)
        print(maxLength)