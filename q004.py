#project-euler q004
#largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(param):
    string = str(param)
    string2= string[::-1]
    if string == string2:
        return True
    return False

maxValue = 0
for i in range(900,1000):
    for j in range(900,1000):
        product = i*j
        if isPalindrome(product):
            print(product,"is Palindrome")
            if product>maxValue:
                maxValue = product
print(maxValue)
