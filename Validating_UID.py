# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for i in range(0, int(input())):
    s = input()
    match = re.search(r'^(?=(?:[a-z\d]*[A-Z]){2})(?=(?:\D*\d){3})(?:([a-zA-Z\d])(?!.*\1)){10}$', s)
     
    if match:
        print("Valid")
    else:
        print("Invalid")
#^: Start
#(?=(?:[a-z\d]*[A-Z]){2}): Lookahead to assert that we have at least 2 uppercase alphabets
#(?=(?:\D*\d){3}): Lookahead to assert that we have at least 3 digits
#(?:([a-zA-Z\d])(?!.*\1)){10}: Match exact 10 alphanumeric characters. Negative lookahead is to assert that we don't have anything repeating anywhere.
#$: End