# 1일이 일요일인 달수 계산 #2
sundayCount = 0
totalDay = 0
months = [('Jan',31),('Feb',28),('Mar',31),('Apr',30),('May',31),('Jun',30),('Jul',31),('Aug',31),('Sep',30),('Oct',31),('Nov',30),('Dec',31)]
for year in range(1900,2001):
    for month in months:
        if month[0]=='Feb' and year%4==0 and year%100!=0:
            print(year,month[0],month[1]+1,"leap year")
            totalDay=totalDay+month[1]+1
        else :
            print(year,month[0],month[1])
            totalDay=totalDay+month[1]
        print(totalDay,(totalDay-6)%7)
        if (totalDay-6)%7 == 0 and year>1900:
            sundayCount+=1
print(sundayCount)
print(sundayCount-1) #마지막 2000년 12월이 7로 나누어 떨어지는데,(2001년 1월1일이 일요일이라는 의미),이는 계산범위를 벗어남.
