# Main Logic

from student import Student
from trainer import Trainer

def main():
    # for hover like functionality
    s1 = Student(101,"Kiran")

    # for click functionality
    s2= Student(102,"Abhii",20,"Abhi@gmail.com",9087432109)

    # calling student basic info
    s1.student_basic_info()

    # calling student complete info
    s2.student_complete_info()

    # calling calculation functions
    s1.achievement_status() # calling with s2 object is also fine

    # Trainer Functionality
    t1 = Trainer(101,"Ravi")

    # calling basic trainer info
    t1.trainer_info()

    # calling payment functionality
    t1.sessions_payment_cal(s1)

main()