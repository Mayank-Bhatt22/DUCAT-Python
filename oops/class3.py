class Student:
    def __init__(self,roll_no,name,course,contact):
        self.roll_no=roll_no
        self.name=name
        self.course=course
        self.contact=contact


    def get_detail(self):
        D={'Roll_No':self.roll_no,
           'Name':self.name,
           'Course':self.course,
           'contact':self.contact
        }
        return D
        
        
