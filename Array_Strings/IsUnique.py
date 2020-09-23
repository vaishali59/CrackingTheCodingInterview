'''
def isUnique(s):
    #using hasmap
    d={}
    for i in range(len(s)):
        d[s[i]] = d.get(s[i],0)+1
        if d[s[i]]>=2:
            return False
    return True

s = "a"
print(isUnique(s))
'''
def isUnique(s):
    #using list
    d= [0]*128
    for char in s:
        d[ord(char)]+=1
        if d[ord(char)]>=2:
            return False
    return True

s = "Aa"
print(isUnique(s))
