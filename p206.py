def check_format(num):
    if num%10==0:
        if (num//100)%10==9:
            if (num//10**4)%10==8:
                if (num//10**6)%10==7:
                    if (num//10**8)%10==6:
                        if (num//10**10)%10==5:
                            if (num//10**12)%10==4:
                                if (num//10**14)%10==3:
                                    if (num//10**16)%10==2:
                                        return True
    else:
        return False

for i in range(10**9,10**10):
    num = i*i
    if check_format(num):
        print(num, "True", i)
    # else:
    #     print(num)