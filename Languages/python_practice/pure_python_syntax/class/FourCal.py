class FourCal:
    def __init__(self, in1, in2):
        self.opnd1 = in1
        self.opnd2 = in2
    def setdata(self, in1, in2):
        self.opnd1 = in1
        self.opnd2 = in2
    def add(self):
        return self.opnd1 + self.opnd2
    def mul(self):
        return self.opnd1 * self.opnd2
    def sub(self):
        return self.opnd1 - self.opnd2
    def div(self):
        return self.opnd1 / self.opnd2

class SafeFourCal(FourCal):
    def div(self):
        if self.opnd2 == 0:
            return 0
        else:
            return self.opnd1 / self.opnd2

a = SafeFourCal(4, 0)

print("a.div(): ", a.div())
