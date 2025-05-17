def cookies(g,s):
    g.sort()
    s.sort()
    l=0
    r=0
    n=len(s)
    m=len(g)
    while(l<n and r<m):
        if(s[l]>=g[r]):
            l+=1
            r+=1
        else:
            l+=1
    return r
g=list(map(int,input().split(',')))
s=list(map(int,input().split(',')))
print(cookies(g,s))