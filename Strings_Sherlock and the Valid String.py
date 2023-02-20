#!/bin/python3
from collections import defaultdict

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):    
    count = defaultdict(lambda: 0)
    diff = 0
    for letter in s:
        count[letter] += 1
    initial_value = count[s[0]]
    
    for value in count.values():
        if initial_value != value:
            diff += 1
        if diff > 1:
            return 'NO'
        
    return 'YES'
    

if __name__ == '__main__':
    print(isValid('abcdefghhgfedecba'))
