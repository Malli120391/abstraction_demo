class Student:
    def __init__(self, name, rollno, age):
        self.name = name         #public instance variable
        self._rollno = rollno    #protected instance variable
        self.__age=age           #private instance variable
    def __display(self):
            print(f"Hey my self {self.name} {self.__age} years old with rollno {self._rollno} from student class")
    def displayPrivateData(self):
        self.__display()
class Branch(Student):
    #pass
    def show(self):
        print(f"My rollno is {self._rollno}")
#b1=Branch("King", 45, 11)
#b1.show()
"""def showData():
 b1=Branch("Mallesh", 22)
 print(b1.name)
 #print(b1._rollno)
 showData()"""
s1=Student("Malli", 25, 20)
s1.name="Raju"
#s1._rollno=23
#print(s1.__age)
#s1.__display()
#s1.displayPrivateData()
#print(dir(s1))
print(s1._Student__age)
s1._Student__display()
#s1=Student("Malleswara")
#print(s1.name)
#s1.display()
