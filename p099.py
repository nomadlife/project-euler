from math import log
with open('p099_base_exp.txt') as f:
    numbers=[[int(k) for k in i.split(',')] for i in f.read().split()]
max([(i[1]*log(i[0]),idx,i) for idx,i in enumerate(numbers)])