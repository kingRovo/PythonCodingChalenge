class Animal:
    def __init__(self,eyes):
        self.eyes=eyes
class Dog(Animal):
    def __init__(self,eyes,legs):
        Animal.__init__(self,eyes)
        self.legs=legs
    def printD(self):
        print("Dog has: ",self.eyes,"eyes")
        print("Dog has: ",self.legs,"legs")
class Tiger(Dog):
    def __init__(self,eyes,legs):
        Dog.__init__(self,eyes,legs)
    def printT(self):
        print("The tiger has: ",self.eyes,"Eyes")
        print("The tiger has: ",self.legs,"Legs")
D=Dog(2,4)
D.printD()
t=Tiger(2,4)
t.printD()
t.printT()
        
    
