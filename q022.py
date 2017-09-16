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