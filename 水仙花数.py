n=0
for i in range(100,1000):
    c=int(i%10)
    b=int((i//10))%10
    a=int(i//100)
    if int(i)==a**3+b**3+c**3:
        print(i)
        n+=1
print("总共有%d个水仙花数"%(n))