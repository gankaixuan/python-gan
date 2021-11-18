a=int(input("请输入一个数"))
b=int(input("请输入几个数相加"))
sum=0
gan=0
for i in range(1,b+1):
    gan+=a*(10**(i-1))
    sum+=gan
print(sum)


