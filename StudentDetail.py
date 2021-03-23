import functools
class Student:
    def __init__(self,name,R_Num,cls,age):
        self.name =name
        self.R_num = R_Num
        self.cls = cls
        self.age = age
        
    def FindPercentage(self,mrks):
        self.mrks =mrks
        sm =functools.reduce(lambda a,b : a+b,mrks)
        self.per = self.per=(sm/500)*100
    def displayInfo(self):
      
        print("Name : ",self.name)
        print("Roll Num : ",self.R_num)
        print("Course : ",self.cls)
        print("Age : ",self.age)
        print("Marks : ",self.mrks)
        print("Result Percentage % : ",self.per)
        
n =int(input("How Many Students you want to add: "))
li = []
obs =[]
for i in range(n):
    name = input("Student Name : ")
    rn = input("Roll Num : ")
    crs = input("Course : ")
    age = int(input("Age : "))
    li =[int(x) for x in input("Enter 5 Subjects Marks: ").split()]
    
    s  = Student(name,rn,crs,age)
    s.FindPercentage(li)
    obs.append(s)
print("------Student Data------",end="\n\n")
for ob in obs:
    ob.displayInfo()
    print()
    

    
 
