a = [1,2,3]
b = [1,2,3]

if len(a) != len(b):
    print("Not equal")
else:
    for i in range(len(a)):
        if a[i] != b[i]:
            print("Not Equal")
            break
        else:
            print("Equal")