def reverse_a_string(s):
    # return s[::-1]
    #  (or)
    reverse_str = ""
    for ch in s:
        reverse_str = ch + reverse_str
    return reverse_str

print(reverse_a_string("kiranmai"))