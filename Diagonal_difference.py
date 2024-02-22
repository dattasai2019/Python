#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    sum_1 = 0
    sum_2 = 0
    j = 0
    k = len(arr)-1
    for i in range(0, len(arr)):
        sum_1 = sum_1+arr[i][j]
        sum_2 = sum_2+arr[i][k]
        j= j+1
        k=k-1
   
    total = abs(sum_1-sum_2)
    return total
    
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
