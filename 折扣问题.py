amount=int(input("请输入支付金额"))
if 1000>amount:
    print("用户没有折扣，需支付金额为：",amount)
elif 2000>amount>=1000:
    print("用户可以享受九折优惠，需支付金额为："+amount*0.9)
elif 3000>amount>=2000:
    print("用户可以享受八折优惠，需支付金额为："+float(amount*0.8)
elif amount>=3000:
    print("用户可以享受七折优惠，需支付金额为："+float(amount*0.7)