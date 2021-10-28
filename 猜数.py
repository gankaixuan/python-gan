import random
x=random.randint(0,100)
n=1
print(x)
while n<=3:
    y=int(input("请输入一个0到100的整数"))
    if y>x:
        print("小盆友你猜大了哦")
        n+=1
    elif y<x:
        print("大盆友你猜小了哦")
        n+=1
    else:
        print("恭喜你猜对了")
        break
if n>3:
    print("超过三次机会了哦小盆友，你还是没有猜出来呀")
