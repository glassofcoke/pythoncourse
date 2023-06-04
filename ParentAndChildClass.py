class Parent: #Parent Class
    parentAttr = 100

    def __init__(self):
        print("Instantiating Parent")
    def parentMethod(self):
        print("Parent Method")
    def setAttr(self,attr):
        Parent.parentAttr = attr
    def getAttr(self):
        print("Parent attribute: ", Parent.parentAttr)


class Child(Parent):
    def __init__(self):
        print("Instantiating child")
    def childMethod(self):
        print("Child Method")
    def getAttr(self):
        super().getAttr()
        print("Child says hello! ")

c = Child()     #Instantiating Child
c.childMethod()     #Calling Child Method
c.parentMethod()    #Calling Parent Method
c.setAttr (200)     #Set attribute of parent method
c.getAttr()         #Calls attribute from parent method

