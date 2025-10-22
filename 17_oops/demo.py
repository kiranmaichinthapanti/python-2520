# OOPS Basics

data = 10
print(type(data))

# class
class Employee:
    pass

# object
emp_obj = Employee()
print(type(emp_obj))

# Student -> Real World Entity
class Student:
    # attributes / variables
    student_name = "kiran"
    student_email = "kiran@gmail.com"

    # statements
    print("Student Name: ",student_name)
    print("Student Email: ",student_email)

# function (outside the class)
def student_fun():
    # variables
    student_name = "john"
    student_email = "john@gmail.com"
    # statements
    print("Student Name: ",student_name)
    print("Student Email: ",student_email)

# for functions call is must
student_fun()

# Student -> Real World Entity
class Student:
    # attributes / variables
    student_name = "kiran"
    student_email = "kiran@gmail.com"

    # method
    def info(self):
        # student_email = "kiran@gmail.com"
        print("Student Name: ",self.student_name)
        print("Student Email: ",self.student_email)

student_one_obj = Student()
student_two_obj = Student()
student_three_obj = Student()
# Method call is required
student_one_obj.info() # TypeError: Student.info() takes 0 positional arguments but 1 was given
student_two_obj.info()
student_three_obj.info()

# __init__() -> Constructor
class Student:
    # Constructor
    def __init__(self,student_name,student_email):
        self.student_name = student_name
        self.student_email = student_email

    # method
    def info(self):
        # student_email = "kiran@gmail.com"
        print("Student Name: ",self.student_name)
        print("Student Email: ",self.student_email)

kiran_obj = Student("kiran","kiran@gmail.com")
abhi_obj = Student("abhi","abhi@gmail.com")
puppy_obj = Student("puppy","puppy@gmail.com")

kiran_obj.info()
abhi_obj.info()
puppy_obj.info()