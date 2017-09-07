#project-euler q011
#Largest Product in grid

filename = 'q011_data.txt' 
with open(filename) as file_object:
	contents = file_object.read()

	
i=0;max_product=0
while i<17:
	j=0
	while j<20:
		print("position :",i,j,"  ",int(contents[i*3+j*60])*10+int(contents[i*3+j*60+1]))
		k=0
		product=1
		while k<4:
			product=product*(int(contents[i*3+j*60+k*3])*10+int(contents[i*3+j*60+k*3+1]))
			k+=1
		print("product right",product)
		if product>max_product:
			max_product=product
			print("****new max product =",max_product)

		j+=1
	i+=1

	
i=0
while i<20:
	j=0
	while j<17:
		print("position :",i,j,int(contents[i*3+j*60])*10+int(contents[i*3+j*60+1]))	
		k=0
		product=1
		while k<4:
			product=product*(int(contents[i*3+j*60+k*60])*10+int(contents[i*3+j*60+k*60+1]))
			k+=1
		print("product down",product)
		if product>max_product:
			max_product=product
			print("****new max product =",max_product)

	
		j+=1
	i+=1

	
i=0
while i<17:
	j=0
	while j<17:
		print("position :",i,j,int(contents[i*3+j*60])*10+int(contents[i*3+j*60+1]))
		k=0
		product=1
		while k<4:
			product=product*(int(contents[i*3+j*60+k*63])*10+int(contents[i*3+j*60+k*63+1]))
			k+=1
		print("product diagonal",product)
		if product>max_product:
			max_product=product
			print("****new max product =",max_product)
		j+=1
	i+=1
	
i=3
while i<20:
	j=0
	while j<17:
		print("position :",i,j,int(contents[i*3+j*60])*10+int(contents[i*3+j*60+1]))
		k=0
		product=1
		while k<4:
			product=product*(int(contents[i*3+j*60+k*57])*10+int(contents[i*3+j*60+k*57+1]))
			k+=1
		print("product diagonal-2",product)
		if product>max_product:
			max_product=product
			print("****new max product =",max_product)
		j+=1
	i+=1	
	
	
print("max_product is ",max_product)