for i in range(1,100):
    for j in range(1,i):
        #fraction = j/i
        for n in str(i):
            if n in str(j) and not n == "0" and not len(str(j))==1:
                new_j = str(j).replace(n,"",1)
                new_i = str(i).replace(n,"",1)
                if not (new_i == "0" or new_j == "0"):
                    #print(j,i,n, new_j,"/",new_i,end=',')
                    if j/i == int(new_j)/int(new_i):
                        print(j,i,n, new_j,"/",new_i,"True")
