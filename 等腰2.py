i=1
j=1
k=1
while(i<=4):
    j=1
    k=4
    while(k>=i):
        print(" ",end="")
        k-=1
    while(j<=i):
        print(" *",end="")
        j+=1
    print("\n")
    i+=1