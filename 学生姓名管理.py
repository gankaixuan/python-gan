print("="*50,"gan","="*50)
class Student:
    def __init__(self):
        self.student_li=[]
    def welcome(self):
        print("欢迎使用无敌好用的学生管理学习系统")
        print("1:添加")
        print("2:删除")
        print("3:退出")
        print("0:显示")
        while True:
            option = input("请输入功能\n")
            if option == '1':
                self.add_student()
            elif option == '2':
                self.de_student()
            elif option == '3':
                print("已退出程序")
                break
            elif option == '0':
                self.go_student()
    def add_student(self):
        add_student=input("请输入要添加的学生")
        self.student_li.append(add_student)
        print("学生添加成功")
    def de_student(self):
        x=str(input("请输入要删除的名字"))
        for i in self.student_li:
            if x ==i:
                self.student_li.remove(i)
                flag=1
                break    #如果有同名的就删第一个    如果想删掉全部同名的删掉就行
        if flag ==1:
            print("学生删除成功")
        else:
            print("没有这位学生的名字")
    def go_student(self):
        print(self.student_li)
u1=Student()
u1.welcome()




