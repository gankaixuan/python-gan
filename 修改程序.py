a=int(input("请输入2-22中的某个数"))
if a<=20 and a>=2:
    i=0
    while (i>=0 and i<a):
        if i==0 or i==a-1:
            print(" * "*a)
        else:
            print(" * "+"   "*(a-2)+" * ")
        i=i+1