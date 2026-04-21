# Given a string word to which you can insert letters "a", "b" or "c" anywhere and any number of times, return the minimum number of letters that must be inserted so that word becomes valid.
# A string is called valid if it can be formed by concatenating the string "abc" several times.

def addMinimum(word):
    count = 0
    prev = 'z'
    for ch in word:
        if ch <= prev:
            count += 3
        prev = ch
    return count - len(word)

print(addMinimum('b'))
print(addMinimum('aaa'))
print(addMinimum("ab"))
