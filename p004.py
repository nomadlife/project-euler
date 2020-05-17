# Q004 Largest palindrome product
# largest palindrome made from the product of two 3-digit numbers.

maxValue = 0
for i in range(900, 1000):
    for j in range(900, 1000):
        product = i*j
        if str(product) == str(product)[::-1]:
            if product > maxValue:
                maxValue = product
print(maxValue)
