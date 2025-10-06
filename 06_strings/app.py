# Enhanced Student Grade Tracker Solution

print("="*50)
print("          Enhanced Student Grade Tracker")
print("="*50)

# Student ID
student_id_valid = False

while not student_id_valid:
    student_id = input("Enter ID: ")
    
    # check for positive number & non-alphabet (-5)[index of '-' is zero 5 is 1]
    if student_id.startswith("-") and student_id[1:].isdigit():
        print("Please Enter Positive Numbers Only")
    elif student_id.isdigit():
        student_id = int(student_id)
        if student_id > 0:
            student_id_valid = True
        else:
            print("Zero Not Allowed")
    else:
        print("Enter Numbers Only")

print(student_id)

# Student Name
student_name_valid = False

while not student_name_valid:
    student_name = input("Enter Name: ")
    student_name = student_name.strip()
    only_letters = student_name.replace(" ","")

    if only_letters == "":
        print("Name Connot be empty")
    elif not only_letters.isalpha():
        print("Enter Alphabets Only")
    elif len(only_letters) < 3:
        print("Name should have at least 3 characters")
    else:
        student_name = student_name.title()
        print(student_name)
        student_name_valid = True

# System Generated Email
first_name = student_name.split()[0].lower()
system_email = f"{first_name}.{student_id}@edify.edu"
print("System Generated Email:", system_email)

# Course Fee Calculation
course_fee = float(input("Enter Course Fee: "))

if course_fee <= 0:
    print("Course Fee must be greater than zero")
else:
    coupon = input("Enter Coupon Code: ").strip()

    if coupon.upper() == "PROMO":
        if course_fee > 5000:
            course_fee -= 5000
        else:
            course_fee = 0
        print("PROMO Applied : 5000 Discount!")

    print(f"Final Course Fee : {course_fee}")