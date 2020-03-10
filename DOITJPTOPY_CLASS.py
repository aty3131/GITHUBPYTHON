
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    """def setdata(self, first, second):
        self.first = first
        self.second = second
    """
    def add(self):
        result= self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
class SafeFourCal(FourCal) :
    def div(self):
        if self.second == 0 :
            return 0
        else :
            return self.first / self.second
class FailFourCal(FourCal) :
    def mul(self):
        if self.second == 0 :
            return "Fail"
        else :
            return self.first * self.second
"""
a = FourCal()
b = FourCal()
print(type(a))
a.setdata(4,2)
b.setdata(3,7)
print(a.first)
print(a.second)
print(b.first)
print(id(a.first))
print(id(b.first))
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print(b.add())
print(b.mul())
"""
"""
a = FourCal(4, 2)
print(a.first)
print(a.second)
print(a.add())
print(a.div())
a = MoreFourCal(4, 2)
print(a.add())
print(a.pow())
a = SafeFourCal(4, 0)
print(a.div())
"""
a = FailFourCal(4, 0)
print(a.mul())