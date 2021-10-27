import random
x=random.randint(0,100)
while True:
    y=int(input("请输入一个数"))
    if y>x:
        print("小盆友你猜大了哦")
    elif y<x:
        print("大盆友你猜小了哦")
    else:
        print("恭喜你猜对了")
        break
