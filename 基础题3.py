a=str(input("请输入一个字符串"))
x=y=z=0
for i in a:
    if i.islower()==True:
        x+=1
    elif i.isupper()==True:
        y+=1
    else:
        z+=1
print("小写字母有%d个，大写字母有%d个,其他字符有%d个"%(x,y,z))
