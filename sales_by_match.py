'''
https://www.hackerrank.com/contests/mountblue-technologies/challenges/sock-merchant/problem
'''
#!/bin/python

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    count = Counter(ar)
    pairs = 0
    for i in count:
        if(count[i]>1):
            pairs += count[i]/2;
    return pairs
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

