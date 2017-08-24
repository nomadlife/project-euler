#project-euler q011
#Largest Product in grid

# 178920th person to have solved this problem.

filename = 'q011_data.txt'
with open(filename) as file_object:
	lines = file_object.readlines()
m=len(lines)

numbers=[]
for line in lines:
	print(line.split())
	numbers.append(line.split())



max_product=0
print("max_product is ",max_product)
