def isAcronym(words,s):
    if len(s)!=len(words):
        return False
    for i in range(len(words)):
        if words[i][0]!=s[i]:
            return False
    return True 
words=input()
s=input()
print(isAcronym(words,s))
        