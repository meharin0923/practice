s=[1,2,3,5]
missing=[]
for i in (range(min(s),max(s)+1)):
    if i not in s:
        missing.append(i)
print(missing)    
    #timecomplexity :O(n)
