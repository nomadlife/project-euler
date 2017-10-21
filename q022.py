# Q022 Names scores
# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53
# 938th name in the list, COLIN would obtain a score of 938 × 53 = 49714.
# What is the total of all the name scores in the file?

filename = 'q022_data.txt'
with open(filename) as file_object:
    contents = file_object.read()
contents=contents.replace('"','')
names=contents.split(',')
names.sort()

grand_total =0
for idx,val in enumerate(names):
    print(idx+1,val,end=' ')
    total=0
    for i in val:
        print(ord(i)-64,end=',')
        total=total+ord(i)-64
    print("total:",total,end=',')
    grand_total+=total*(idx+1)
    print(grand_total)
