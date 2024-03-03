# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(0, int(input())):
    s = input()
    match = re.search(r'^(?!\d*(\d)(-?\1){3})[456][0-9]{3}(-?[0-9]{4}){3}$', s)
    
    if match:
        print("Valid")
    else:
        print("Invalid")