x=int(input("请输入一个整数"))
y=int(input("请输入一个整数"))
z=int(input("请输入一个整数"))
if x>y>z:
    print("您输入的三个数是：",z,y,x)
elif x>z>y:
    print("您输入的三个数是：",y,z,x)
elif y>x>z:
    print("您输入的三个数是：",z,x,y)
elif y>z>x:
    print("您输入的三个数是：",x,z,y)
elif z>x>y:
    print("您输入的三个数是：",y,x,z)
else:
    print("您输入的三个数是：",x,y,z)