a=int(input("请输入2-20的整数"))
for x in range(a):
    if x ==0 or x==a-1:
        print(" * "*a)
    else:
        print(" * "+"   "*(a-2)+" * ")