'''
https://www.hackerrank.com/challenges/camelcase/problem?isFullScreen=false
'''

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):
    count = 0
    for i in s:
        if ord(i)>64 and ord(i)<91:
            count = count+1
    return count + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()

