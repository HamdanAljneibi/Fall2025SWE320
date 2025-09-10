class Rectangle:
    """This class describes a Rectangle"""
    #constructor: attributes
    def __init__(self):
        self.length = 0.0
        self.breadth = 0.0
    #functions
    def getlength(self):
        return self.length
    def getbreadth(self):
        return self.breadth
    def setlength(self, newlength):
        self.length = newlength
    def setbreadth(self, newbreadth):
        self.breadth = newbreadth
    def areaRectangle(self):
        area = self.length * self.breadth
        return area


#Create the objects
RedRectangle = Rectangle()
RedRectangle.setlength(20)
RedRectangle.setbreadth(25.2)
print("The area of Red Rectangle is", RedRectangle.areaRectangle())
BlueRectangle = Rectangle()
BlueRectangle.setlength(12.5)
BlueRectangle.setbreadth(15.5)
print("The area of Blue Rectangle is", BlueRectangle.areaRectangle())
print("The length of the Blue Rectangle is:", BlueRectangle.getlength())
print("The breadth of the Blue Rectangle is:", BlueRectangle.getbreadth())