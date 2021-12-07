class People:
    __name="gkx"
    __age = 1000
    __genderage = 5
    @staticmethod
    def getage():
        print(People.__age)
    def getname():
        print(People.__name)
people1=People()
People.getage()
People.getname()
p