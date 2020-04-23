from ass2module import *

class Marks(Student):
    
    def __init__(self, prn, name, dob, email, contact, marks):
        Student.__init__(self, prn, roll, name, dob, email, contact)
        self.marks = marks
        

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, marks):
        if isinstanceof(Marks,marks):
            self.__marks = marks
        else:
            print(mks)            
            self.__marks = mks

class MarksData(object):
    @staticmethod
    marks = {}
    def addStudent():
        prn = input("\nEnter PRN: ")
        StudentData.roll = StudentData.roll + 1
        name = input("\nEnter the name: ")
        dob = input("\nEnter Date of Birth")
        email = input("\nEnter your email id: ")
        contact = input("\nEnter the contact number: ")
        
        while true:
            
            OOT= input("Enter marks of OOT : ")
            if OOT>0 and OOT<=100 :
                marks.update('OOT' : OOT)  
                break  
            else:
                continue
            
        while true:
            
            ME= input("Enter marks of ME : ")
            if ME>0 and ME<=100 :
                marks.update('ME' : ME)  
                break  
            else:
                continue

        while true:
            
            EI= input("Enter marks of EI : ")
            if EI>0 and EI<=100 :
                marks.update('EI' : EI)  
                break  
            else:
                continue
        for k,v in marks.items():
            print(k,":",v)
        m=Marks(prn,name,dob,email,contact,marks)
          

        
