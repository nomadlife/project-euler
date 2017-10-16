# Q008
#Largest Product in Series

from urllib.request import urlretrieve
urlretrieve("https://raw.githubusercontent.com/nomadlife/project-euler/master/q008_data.txt", "q008_data.txt")

with open("q008_data.txt") as file_object:
    lines = file_object.readlines()

string=''
for line in lines:
    string=string+line.rstrip()

max_value = 0
i=0
loop = len(string)-13
while i < loop:
    product =1
    for j in string[i:i+13]:
        product = product * int(j)
    if product > max_value:
        max_value = product
        print("loop:",i,"max:",product)
    i+=1
print(max_value)
