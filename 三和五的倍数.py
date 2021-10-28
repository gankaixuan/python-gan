n=0
a=0
while n<=100:
    n+=1
    if n%3==0 and n%5!=0:
        print(n)
        a+=1
print("总共有",a,"个数")
