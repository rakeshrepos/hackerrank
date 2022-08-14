
'''
https://www.hackerrank.com/contests/mountblue-technologies/challenges/breaking-best-and-worst-records/problem
'''
#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    highest = scores[0]
    lowest = scores[0]
    highest_count = 0
    lowest_count = 0
    count = []
    
    for i in range(len(scores)):
        if highest<scores[i]:
            highest_count += 1
            highest = scores[i]
        if lowest>scores[i]:
            lowest_count +=1
            lowest = scores[i]
    
    count.append(highest_count)
    count.append(lowest_count)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    scores = map(int, raw_input().rstrip().split())

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

