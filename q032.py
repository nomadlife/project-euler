#032 pandigital product

def get_next_permutation(string):
    i=len(string)-2
    while i >= 0:
        if string[i] < string[i+1]:
            target = sorted(string[i:])
            new_num = target.pop(target.index(string[i])+1)
            last_nums = ''.join(target)
            return string[:i] + new_num + last_nums
        i-=1

test = "123456789"
m=len(test)
total = []
while not test == None:
    for i in range(1,m):
        str1=test[0:i]
        for j in range(i+1,m):
            str2=test[i:j]
            str3=test[j:m]
            if int(str1)*int(str2)==int(str3):
                print(str1,str2,str3)
                total.append(int(str3))
    test = get_next_permutation(test)
print(total)
print(sum([x for i,x in enumerate(total) if total[:i].count(x)==1]))