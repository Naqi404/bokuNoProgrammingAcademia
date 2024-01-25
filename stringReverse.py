def reverseString(s):
    r = len(s)-1
    out = []

    while r>=0:
        out.append(s[r])
        r-=1
        
    return out
    
print(reverseString(['h','e','l','l','o']))
