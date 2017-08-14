#project-euler q002
#sum fibonachi series under 4,000,000 where even-valued term.

previous_i=1;i=1;total=0
while i<4000000 :
	print("loop ",i)
	if i%2==0 :
		total=total+i
		print("total is ",total)
	next_i=previous_i+i
	previous_i=i
	i=next_i

print(total)
