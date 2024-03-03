#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
    
matrix_list = list(zip(*matrix))

s = ''.join(''.join(i) for i in matrix_list)

print(re.sub(r'\b\W+\b', ' ', s))
