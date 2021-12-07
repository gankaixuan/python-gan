class People:
    def __init__(self,h):
        print(self)
        self.name=h
    def show(self):
        print(self,self.name)
p=People("222")
p.show()