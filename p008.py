# Q008 Largest Product in Series
# Find the thirteen adjacent digits in the 1000-digit number
# that have the greatest product.

with open("p008_data.txt") as file_object:
    lines = file_object.readlines()

string = ''
for line in lines:
    string = string+line.rstrip()

max_value = 0
i = 0
loop = len(string)-13
while i < loop:
    product = 1
    for j in string[i:i+13]:
        product = product * int(j)
    if product > max_value:
        max_value = product
        print("loop:", i, "max:", product)
    i += 1
print(max_value)
