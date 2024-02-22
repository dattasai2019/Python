# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = input()
k = input()

pattern = re.compile(k)

m = pattern.search(s)

if m:
    while m:
        print((m.start(), m.end()-1))
        i = m.start()+1
        m = pattern.search(s, i)
else:
    print((-1, -1))
