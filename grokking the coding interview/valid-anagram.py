##############
#
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
##############

def sol(a, b):
    count = {}

    for char in a:
        count[char] = count.get(char, 0)+1
    for char in b:
        if char not in count:
            return False
        count[char] = count.get(char, 0)-1
        if count[char] == 0:
            del count[char]

    return not bool(count)


print(sol('cat', 'rat'))
print(sol('asad', 'sada'))
