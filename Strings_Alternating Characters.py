#!/bin/python3

import math
import os
import random
import re
import sys

def alternatingCharacters(s):
    number_of_deletion = 0
    if len(s) < 2:
        return 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            number_of_deletion+=1
    return number_of_deletion

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
