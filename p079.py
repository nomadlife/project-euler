#p079
with open('p079_keylog.txt') as file:
    codes = [line.rstrip() for line in file.readlines()]

def sort(a,b):
    if result[a]>result[b]:
        temp = result[a]
        result[a] = result[b]
        result[b] = temp
    
result={}
for code in codes:
    for j in code:
        if (j) not in result:
            result[j] = len(result)+1
    sort(code[0],code[1])
    sort(code[1],code[2])
	
sorted(result, key=result.get)