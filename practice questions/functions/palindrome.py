def palindrome(s):
    s = s.lower().replace(" ","")
    
    return "Palindrome" if s == s[::-1] else "Not Palindrome"
        
    
s = input("Enter String: ")
print(palindrome(s))