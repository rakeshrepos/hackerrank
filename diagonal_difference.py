'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix  is shown below:
1 2 3
4 5 6
9 8 9  

Function description

Complete the  diagonalDifference function in the editor below.

diagonalDifference takes the following parameter:

int arr[n][m]: an array of integers
'''

#!/bin/python

import math
import os
import random
import re
import sys
#import numpy as np

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(n,arr):
    main =0
    second =0
    l=len(arr[0])
    for i in range(n):
        main +=arr[i][i]
        second +=arr[i][l-i-1]
    dif = abs(main-second)
    return dif
