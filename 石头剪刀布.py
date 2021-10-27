import random
computer=random.randint(0,2)
while True:
    player=int(input("请出石头（0）剪刀（1）布（2）"))
    if (player==0 and computer==0)or(player==1 and computer==1)or(player==2 and computer==0):
        print("我出的是：%s"%player+",计算机出的是%s"%computer)
        print("心有灵犀，再来一遍")
    elif(player==0 and computer==1)or(player==1 and computer==2)or(player==2 and computer==0):
        print("我出的是：%s"%player+",计算机出的是%s"%computer)
        print("你赢了，计算机太弱了")
        break
    else:
        print("我出的是：%s"%player+",计算机出的是%s"%computer)
        print("计算机你赢了")