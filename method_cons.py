class DemoClass:
    a=10

    def __init__(self):
        print("Welcome")
    def showvalue(self):
        self.c=self.a*self.a
        print(self.c)

    def showvalue1(self):
        print("Welcome to wscubetech")



obj=DemoClass()
obj.showvalue()
obj.showvalue1()