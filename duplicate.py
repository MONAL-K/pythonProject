l=[1,1,2,3,5,6,3,1]
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if l[i]==l[j]:
            print(l[i])