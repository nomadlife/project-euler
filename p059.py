# p059 XOR decryption
with open('p059_cipher.txt') as file_object:
    codes = file_object.read().rstrip().split(',')

key=''
for idx in range(3):
    maxValue =[]
    for k in range(97,123):
        count=0
        for i,j in enumerate(codes):
            if i%3==idx:
                if int(j)^k in range(65,123):
                    count+=1
        maxValue.append([count,chr(k)])
    key+=max(maxValue)[1]

total=0
for i,v in enumerate(codes):
    val=int(v)^ord(key[i%3])
    total+=val
print(total)