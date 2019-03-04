#p079 Passcode derivation
with open('p079_keylog.txt') as file:
    codes = [line.strip() for line in file.readlines()]
    
def sort(a,b):
    if pw[a]>pw[b]:
        pw[a],pw[b] = pw[b],pw[a]

pw={}
for code in codes:
    for j in code:
        if (j) not in pw:
            pw[j] = len(pw)+1
    sort(code[0],code[1])
    sort(code[1],code[2])
	
print(sorted(pw, key=pw.get))