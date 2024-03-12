class mlops:
    def __init__(self,totalStudents):
        self.totalStudents = totalStudents

    def getTotalStudents(self):
        return self.totalStudents
    
    def addStudent(self):
        self.totalStudents += 1

    def removeStudent(self):
        self.totalStudents -= 1

    def getClassName(self):
        return "Machine Learning Operations (CS-B)"

mlopsObj = mlops(5)
print(mlopsObj.getTotalStudents())
print(mlopsObj.getClassName())
print('hello world')