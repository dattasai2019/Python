# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f'Start : {tag}')
        for attr in attrs:
            print("-> {} > {}".format(attr[0], attr[1]))  
    def handle_endtag(self, tag):
        print(f'End   : {tag}')
    def handle_startendtag(self, tag, attrs):
        print(f'Empty : {tag}')
        for attr in attrs:
            print("-> {} > {}".format(attr[0], attr[1]))
           
n = int(input())
parser = MyHTMLParser()
for _ in range(0, n):
    parser.feed(input())