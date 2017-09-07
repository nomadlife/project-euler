#project-euler q011
#Largest Product in grid

filename = 'q011_data.txt'
with open(filename) as file_object:
	lines = file_object.readlines()

numbers=[]
for line in lines:
	print(line.split())
	numbers.append(line.split())

max_product=0
for i in range(20):
    for j in range(20):
        
        #가로숫자 4개 곱
        product =1
        if j+4 < 20:
            for k in range(0,4):
                product *= int(numbers[i][j+k])
            if product >max_product:
                max_product = product
          
        #세로숫자 4개 곱
        product =1
        if i+4 < 20:
            for k in range(0,4):
                product *= int(numbers[i+k][j])
            if product >max_product:
                max_product = product
        
        #대각선(↘)숫자 4개 곱
        product =1
        if i+4 < 20 and j+4 < 20:
            for k in range(0,4):
                product *= int(numbers[i+k][j+k])
            if product >max_product:
                max_product = product
        
        #대각선(↙)숫자 4개 곱
        product =1
        if i+4 < 20 and j+4 < 20 and j >= 3:
            for k in range(0,4):
                product *= int(numbers[i+k][j-k])
            if product >max_product:
                max_product = product
         
print("max_product is ",max_product)

