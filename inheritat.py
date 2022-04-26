class A:
    def displayA(self):
        print("Welcome to wscubetech A")


class B:
    def displayB(self):
        print("Welcome to wscubetech B")

class C(A,B):
    def displayC(self):
        print("Welcome to wscubetech C")




obj=C()
obj.displayA()
obj.displayB()
obj.displayC()