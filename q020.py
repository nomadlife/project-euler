#100까지 계산
def get_factorial(number):
    product=1
    while True:
        if number <=1 :
            return product
        product=product*number
        number=number-1

result=get_factorial(100)
print(result)
string=str(result)

total=0
for i in string:
    total=total+int(i)
print(total)
