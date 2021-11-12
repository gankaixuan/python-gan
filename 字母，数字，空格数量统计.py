s=input("请输入一个字符串：")
a=0
b=0
c=0
d=0
for i in range(len(s)):
    if s[i].isspace()==True:
        a+=1
    elif s[i].isalpha()==True:
        b+=1
    elif s[i].isdigit()==True:
        c+=1
    else:
        d+=1
print("空格的数量为：",a)
print("字母的数量为：",b)
print("数字的数量为：",c)
print("其他字符的数量为：",d)