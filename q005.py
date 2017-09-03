#project-euler q005
#The smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#LCM

def getGCD(num1,num2):
    for j in range(1,num2+1):
        if num1%j==0 and num2%j==0:
            g=j
    return g

lcm=1
for i in range(1,21):
    gcd = getGCD(lcm,i)
    lcm = lcm*i/gcd
    print(i,gcd,lcm)
