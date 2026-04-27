def count_consonants(s):
    count = 0
    vowels = "aeiou"
    for ch in s.lower():
        if ch not in vowels:
            count+=1
    return count

s= input("Enter string: ")
print("consonants count in string is : ", count_consonants(s))