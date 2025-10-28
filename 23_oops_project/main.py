from student import Student
from trainer import Trainer
# from admin import Admin

def main():
    
    # create a student
    s = Student(101,"John",20,"john@gmail",909090)

    # display student
    s.person_complete_info()

    # calling calculation functions
    s.achievement_status() # calling with s2 object is also fine

    # Create a Trainer Functionality
    t = Trainer(900,"Ravi",30,"ravi@gmail",888888)

    # display trainer
    t.person_complete_info()

    # calling payment functionality
    t.sessions_payment_cal(s)

    # dispaly admin
    # a.person_complete_info()

    # a.admin_video()

main()