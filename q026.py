#q026
# longest recurring cycle in its decimal fraction part

from decimal import *

def get_cycle_string(string):
    length = len(string)
    for i,v in enumerate(string):
        end=int(string.find(v,i+1))
        while end != -1 and end < length*0.5:
            target = string[i:end]
            target_len = end-i
            test=string[end:end+target_len]
            if target == test and string.count(target)*target_len > length*0.9:
                return target
            else :
                end=int(string.find(v,end+1))

decimalSize=2000
getcontext().prec = decimalSize
max_length=0
for d in range(1,1000):
    string=str(Decimal(1)/Decimal(d))
    string=string[string.find(".")+1:]
    cycle = get_cycle_string(string)
    if not cycle == None and len(cycle)>max_length:
        max_length = len(cycle)
        print(d,max_length)
