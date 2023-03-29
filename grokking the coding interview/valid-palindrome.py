# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.
import re


def sol(s):
    alpha_num_string = re.sub('\W+', '', s.lower())

    return alpha_num_string == alpha_num_string[::-1]


print(sol('Hello! My name is Asad. 11234!!@#$'))
print(sol('dsa12@21 asd'))
