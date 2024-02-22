def merge_the_tools(string, k):
    # your code goes here
    
    for i in range(0, len(string), k):
        p=""
        for char in string[i:i+k]:
            if char not in p:
                p = p+char
        print(p)
        
        
    
    
