#project-euler q008
#Largest Product in Series

from urllib.request import urlretrieve
urlretrieve("https://raw.githubusercontent.com/nomadlife/project-euler/master/q008_data.txt", "q008_data.txt")

with open("q008_data.txt") as file_object:
    lines = file_object.readlines()

string=''
for line in lines:
    string=string+line.rstrip()
print(string)

max_value = 0
for i in range(0,len(string)):
    print(i,end=":")
    product =1
    for j in range(i,i+13):
        print(string[j],end=',')
        product = product * int(string[j])
    print(product)
    if product > max_value:
        max_value = product
    if i+13 == len(string):
        break
print(max_value)