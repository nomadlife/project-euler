# Q022 Names scores
# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53
# 938th name in the list, COLIN would obtain a score of 938 × 53 = 49714.
# What is the total of all the name scores in the file?

with open('q022_data.txt') as data:
    names = data.read().replace('"','').split(',')
names.sort()

grand_total =0
for idx,val in enumerate(names):
    total=0
    for i in val:
        total=total+ord(i)-64
    grand_total+=total*(idx+1)
print(grand_total)
