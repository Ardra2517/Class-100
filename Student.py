class Student(object):
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    
    def readName(self):
        print("My Name = ",self.name)
    
    def readAge(self):
        print("My Age = ",self.age)
    
    def readGrade(self):
        print("My Grade = ",self.grade)
    
   
Ardra=Student('Ardra',13,'8th')

print(Ardra.readName(),Ardra.readAge(),Ardra.readGrade())