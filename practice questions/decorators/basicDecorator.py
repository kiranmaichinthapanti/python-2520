def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase
def myfunction():
    return "Hello kiran"

print(myfunction())


def squareNumber(func):
    def wrapper():
        return func() ** 2
    return wrapper

@squareNumber
def sfunction():
    return 4

print(sfunction())