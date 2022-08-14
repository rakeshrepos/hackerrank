'''
https://www.hackerrank.com/contests/mountblue-technologies/challenges/quicksort1
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quickSort(arr):
    # Write your code here
    left = []
    right = []
    p = arr[0]

    for i in arr:
        if i > p:
            right.append(i)
        elif i<p:
            left.append(i)

    left.append(p)
    left.extend(right)
    return left

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

