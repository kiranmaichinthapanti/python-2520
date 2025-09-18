# means Comment, python will skip execution of ths line
# We used script mode to execute below code

# Syntax (Rules)
print(9) # 9 is numeric
#print(good, morning) # SyntaxError: invalid syntax, Perhaps you forgot a comma?
# good morning is text data
# in python rule is, if you have text data then we need to enclose that in "" or ''
print("good morning")
print('good morning')

# print(hello) # NameError: name 'hello' is not defined. Did you mean: 'help'?
hello = "hello hi"
print(hello)

# name is identifier

#class = "10th Standard" # SyntaxError: invalid syntax ===> class is a keyword
classes = "10th Standard"
print(classes)


# Identifiers
data = "hello good morning"
print(data)
# 2day_data = "hello"  # invalid as starts with digit
# print(2day_data)
_data = "hello"
print(_data)

# $data = "hello" # SyntaxError: invalid syntax cannot have $ only Underscore(_) allowed
# print(_data)

# Improper way of using Identifiers
x = "Ravi"
y = 30
z = "Python"

# Proper way of using Identifiers
student_name = "Ravi"
student_id = 30
student_enrolled_course = "python"
