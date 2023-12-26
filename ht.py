m=int(input())
while True:
    for i in range(2,m):
        if m%i==0:
            m=m+1
            break
    else:
        t=m
        rev=0
        while t!=0:
            d=t%10
            rev=rev*10+d
            t=t//10
        if rev==t:
            print(m)
            break
        else:
           m=m+1