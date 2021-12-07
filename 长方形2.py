class C:
    def area(self):
        self.long=10
        self.wide=15
        x = self.long * self.wide
        return x
    def s(self):
        y = (self.long+self.wide)*2
        return y
c = C()
print(c.area())
print(c.s())


