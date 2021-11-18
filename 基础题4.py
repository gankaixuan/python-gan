a = int(input("请输入第一个整数："))
b = int(input("请输入第二个整数："))
c = int(input("请输入第三个整数："))
if a >  b > c:
    print(a,b,c)
elif a > c > b:
    print(a, c, b)
elif b > a > c:
	print(b, a, c)
elif b > c > a:
	print(b, c, a)
elif c > a > b:
	print(c, a, b)
else:
	print(c, b, a)
