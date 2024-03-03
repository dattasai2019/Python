# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def match(s):
    s1 = s.group(0)
    if s1 =='&&':
        return 'and'
    else:
        return 'or'

for _ in range(int(input())):
    i = input()
    code = re.sub(r'(?<=\s)(&&)(?=\s)|(?<=\s)(\|\|)(?=\s)', match, i)
    print(code)
