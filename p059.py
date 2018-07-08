# p059 XOR decryption
keyLength=3
for keyNum in range(keyLength):
    string='abcdefghijklmnopqrstuvwxyz'
    test=contents
    maxValue =[]
    for k in string:
        count=0
        for i,j in enumerate(test):
            if i%3==keyNum:
                val= int(j)^ord(k)
                if chr(val) in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ':
                    count+=1
        maxValue.append([count,k])
    print(max(maxValue))