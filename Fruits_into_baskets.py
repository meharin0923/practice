#BRUTE FROCE METHOD
'''
def totalfruits(f):
    n=len(f)
    maxLen=0
    for i in range(0,n):
        s=set()
        for j in range(i,n):
            s.add (f[j])
            if(len(s)>2):
                break
            maxLen=max(maxLen,j-i+1)
    return maxLen
f=input()
print(totalfruits(f))
'''#Time limit exceeded
#SLIDING WINDOW METHOD

def totalfruits(f):
    n=len(f)
    left=0
    right=0
    maxLen=0
    d={}
    while(right<n):
        if(f[right] in d):
            d[f[right]]+=1
        else:
            d[f[right]]=1
        if(len(d)>2):
            while(len(d)>2):
                d[f[left]]-=1
                if(d[f[left]]==0):
                    del d[f[left]]
                left+=1
        maxLen=max(maxLen,right-left+1)
        right+=1
    return maxLen
f=input()
print(totalfruits(f))
