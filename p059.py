# p059 XOR decryption
with open('p059_cipher.txt') as file_object:
    contents = file_object.read().rstrip().split(',')
    
for keyNum in range(3):
    maxValue =[]
    for k in range(97,123):
        count=0
        for i,j in enumerate(contents):
            if i%3==keyNum:
                if int(j)^k in range(65,123):
                    count+=1
        maxValue.append([count,chr(k)])
    print(max(maxValue))