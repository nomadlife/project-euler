#q018 functions

def find_route_down(i,j,total=0,path=''):
	total=total+numbers[i][j]
	path=path+str(numbers[i][j])+";"
	if i==m-1:
		print(total,path)
		return total,path
	else :
		if numbers[i+1][j] < numbers[i+1][j+1]:
			j+=1
	i+=1
	find_route_down(i,j,total,path)

def find_route_up(i,j,total=0,path=''):
	total=total+numbers[i][j]
	path=path+str(numbers[i][j])+";"
	if i==0:
		print(total,path)
		return total,path
	else :
		if numbers[i-1][j] < numbers[i-1][j-1]:
			j-=1
	i-=1
	find_route_up(i,j,total,path)

def biggest_sum_with_path(i=0,j=0):
	# not completed
	if i==m-1:
		return numbers[i][j],numbers[i][j]
	else :
		num1=biggest_sum_with_path(i+1,j)
		num2=biggest_sum_with_path(i+1,j+1)
		if num1>num2:
			return int(numbers[i][j])+int(num1),numbers[i][j]+num1
		else :
			return int(numbers[i][j])+int(num2),numbers[i][j]+num2

def biggest_path(i=0,j=0):
	if i==m-1:
		return numbers[i][j]
	else :
		num1=biggest_path(i+1,j)
		num2=biggest_path(i+1,j+1)
		if num1>num2:
			return numbers[i][j]+","+num1
		else :
			return numbers[i][j]+","+num2

def biggest_sum(i=0,j=0):
	if i==m-1:
		return numbers[i][j]
	else :
		num1=biggest_sum(i+1,j)
		num2=biggest_sum(i+1,j+1)
		if num1>num2:
			return int(numbers[i][j])+int(num1)
		else :
			return int(numbers[i][j])+int(num2)

def decision_two_step(i,j):
	return
