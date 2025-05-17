def jump(n):
    maxind=0
    for i in range(0,len(n)):
        if(i>maxind):
            return False
        maxind = max(maxind,i+n[i])
    return True
n=list(map(int,input().split(",")))
print(jump(n))
