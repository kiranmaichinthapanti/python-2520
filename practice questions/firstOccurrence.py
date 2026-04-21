# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

def firstOccurrence(str1,str2):
    return str1.find(str2)

print(firstOccurrence("happy","app"))


def strstr(str1,str2):
    if str2 == "":
        return 0
    for i in range(len(str1)-len(str2)+1):
        if str1[i:i+len(str2)] == str2:
            return i
    return -1

print(strstr("happy","app"))