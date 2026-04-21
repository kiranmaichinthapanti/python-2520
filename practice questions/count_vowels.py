# Vowels in a string

str1 = input("Enter the string:")
vowels = "aeiouAEIOU"
count = 0
for char in str1:
    if char in vowels:
        count += 1
print(count)

vowels_in_str = [ch for ch in str1.lower() if ch in vowels]
print("Vowels found:", vowels_in_str)
print("Number of vowels:", len(vowels_in_str))

