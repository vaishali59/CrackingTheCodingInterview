def stringCompression(s):
    res=[]
    count = 1
    if len(s)<=1:
        return s
    
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            count+=1
        else:
            res.append(s[i-1])
            res.append(str(count))
            count = 1
            
    res.append(s[i])
    res.append(str(count))
    if len(res)>=len(s):
        return s
    else:
        return "".join(res)

s = "aab"
print(stringCompression(s))

# NOTE : if we take res="" a string then complexity will be slow as
#concatenation operates in O(n2) time, hence we will take list
