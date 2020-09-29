class ArgTest():
    def __init__(self, in1, in2, in3=3):
        self.arg1 = in1
        self.arg2 = in2
        self.arg3 = in3
    def showargs(self):
        print("self.arg1: ", self.arg1)
        print("self.arg2: ", self.arg2)
        print("self.arg3: ", self.arg3)

a = ArgTest(1, in2=2, in3=4)
a.showargs()
