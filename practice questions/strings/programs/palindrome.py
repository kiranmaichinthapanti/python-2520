def if_palindrome(s):
    if s == s[::-1]:
        return "palindrome"
    else:
        return "not palindrome"

s= input("Enter the string:")
print(if_palindrome(s)) 