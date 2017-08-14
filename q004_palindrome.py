#project-euler q004
#largest palindrome made from the product of two 3-digit numbers.


def is_palindrome(number):
	text=str(number)
	size=len(text)-1
	i=0
	while i<size/2:
		if text[i]!=text[size-i]:
			return False
		i=i+1
	return True

i=900;max_falindrome=0
while i<1000:
	j=900
	while j<1000:
		product=i*j
		if is_palindrome(product):
			print(product,"is palindrome")
			if product>max_falindrome:
				max_falindrome=product
			print("max_falindrome is ",max_falindrome)
		j=j+1
	i=i+1
	
