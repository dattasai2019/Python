# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

s = input()

lis = re.findall(r"(?<=[^aeiouAEIOU])([aeiouAEIOU]{2,})(?=[^aeiouAEIOU])", s)

if lis:
    for i in lis:
        print(i)
else:
     print(-1)
