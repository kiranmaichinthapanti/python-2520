def count_vowels_in_string(s):
    # return sum(1 for ch in s.lower() if ch in "aeiou")

    count = 0
    vowels = "aeiou"

    for ch in s.lower():
        if ch in vowels:
            count += 1
    return count

s = input("Enter String: ")
print("vowels count in  string is : ", count_vowels_in_string(s))

def count_each_vowel(s):
    vowels = "aeiou"
    result = {v:0 for v in vowels}

    for ch in s.lower():
        if ch in vowels:
            result[ch] += 1
    return result
print(count_each_vowel("kiranmai"))