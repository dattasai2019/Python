# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

s = input()

m = re.match(r".*?([a-zA-Z0-9])\1", s)

if m:
    print(m.group(1))
else:
    print(-1)
