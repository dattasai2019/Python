# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

inputs = int(input())

for i in range(inputs):
    print(bool(re.search(r"^[+-]?\d*\.\d+$", input())))
