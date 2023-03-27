#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    character_looking_for = None
    special_susbtr_count = n
    for index, value in enumerate(s):
        for cur_index, cur_value in enumerate(s):
            # check for in front character
            if (cur_index + 1 < len(s)-1) and s[cur_index] == s[cur_index+1]:
                special_susbtr_count += 1
            elif (cur_index + 1 < len(s)-1) and (cur_index - 1 > 0) and 
            # check for forward and backward if option
            # if nothing is available then break out of this loop


if __name__ == '__main__':


    result = substrCount(5, 'asasd')
