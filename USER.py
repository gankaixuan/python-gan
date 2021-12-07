class User:
    def __init__(self,n,m,a):
        self.first_name=n
        self.last_name=m
        self.age=a
    def describe_user(self):
        print(self.first_name,self.last_name,self.age)
    def greet_user(self):
        if self.age<=20:
            print("Have a nice day")
        if self.age>20 and self.age<=60:
            print("加油工作，你是最棒的")
        if self.age>60:
            print("早睡早起，健康每一天")
x=str(input("请输入你的姓"))
y=str(input("请输入你的名"))
z=int(input("请输入你的年龄"))
u1=User(x,y,z)
u1.describe_user()
u1.greet_user()




