class Ws:
    def displayinfo(self):
        print("Welcome to wscubetech")



class IIP(Ws):
    def displayinfo(self):
        super().displayinfo()
        print("Welcome to IIP")

obj=IIP()
obj.displayinfo()

