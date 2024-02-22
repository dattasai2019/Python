#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    for i in range(n):
        n=n-1
        for k in range(0, n):
            print(' ', end="")
        for j in range(0, i+1):
            print('#', end="")
        print("\r")
    
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
