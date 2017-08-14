#project-euler q008
#Largest Product in Series

filename = 'q008_data.txt' 
with open(filename) as file_object:
	lines = file_object.readlines()
	
pi_string =''
for line in lines:
	pi_string+= line.rstrip()


i=0;max_product=0
while i<1000:
	print("loop",i)
	j=0;product=1
	while j<13:
		print(pi_string[i+j]+" ",end='')
		product=product*int(pi_string[i+j])
		j+=1
	print("product :",product)
	if product>max_product:
		max_product=product
		print("new max_product :",max_product)
	if i+12==999:
		break
	i+=1
		
print("final max_product :",max_product)