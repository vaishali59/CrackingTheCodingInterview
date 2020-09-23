def oneAway(str1, str2):
    if len(str1)>=len(str2):
        s1=str1
        s2=str2
    else:
        s1=str2
        s2=str1
    d=buildMap(s1,s2)
    print(d)
    return checkEdit(d.values())

def buildMap(s1,s2):
    d={}
    for char in s1:
        d[char]=d.get(char,0)+1
    for char in s2:
        d[char]=d.get(char,0)-1
    return d

def checkEdit(values):
    edit=False
    for count in values:
        if count>1:
            return False
        if count==1:
            if edit:
                return False
            edit=True
    return True

print(oneAway("pale","pales"))
