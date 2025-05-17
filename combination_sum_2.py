def generate(ind,curr,ans,can,tar):
    if(tar==0):
        ans.append(curr.copy())
        return
    if(tar<0 or ind==len(can)):
        return
    curr.append(can[ind])
    generate(ind+1,curr,ans,can,tar-can[ind])
    curr.pop()
    for i in range(ind+1,len(can)):
        if(can[ind]!=can[i]):
            generate(i,curr,ans,can,tar)
            break
def combination(can,tar):
    can.sort()
    curr=[]
    ind=0
    ans=[]
    generate(ind,curr,ans,can,tar)
    return ans
can=list(map(int,input().split()))
tar=int(input())
print(combination(can,tar))
