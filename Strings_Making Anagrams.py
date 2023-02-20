# Strings: Making Anagrams

#!/bin/python3
import os
from collections import defaultdict

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    remainders = defaultdict(lambda: 0)
    
    for s in a:
        remainders[s]+=1
    for s in b:
        remainders[s]-=1
    return sum(abs(remainders[rem]) for rem in remainders)

if __name__ == '__main__':
    print(makeAnagram('cde', 'abc'))