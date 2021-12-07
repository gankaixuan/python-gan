class Student:
    def __init__(self,a,b,c,d,e):
        self.name=a
        self.age=b
        self.chinese=c
        self.math=d
        self.english=e
    def get_name(self):
        print(str(self.name))
    def get_age(self):
        print(int(self.age))
    def get_course(self):
        print(int(max(self.chinese,self.math,self.english)))
x=str(input("请输入姓名"))
y=int(input("请输入年龄"))
z=int(input("请输入语文成绩"))
m=int(input("请输入数学成绩"))
n=int(input("请输入英语成绩"))
s1=Student(x,y,z,m,n)
s1.get_name()
s1.get_age()
s1.get_course()
