class getData(object):
    # init is used for initlization parameters
    def __init__(self):
        self.name=""

    def getString(self):
        self.name=input("Enter the name")

    def printString(self):
        print(self.name.upper())

obj=getData()
#strVal=input("Enter the name \n")
obj.getString()
obj.printString()
