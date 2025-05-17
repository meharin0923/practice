def generate(ind,curr,ans,can,target):
    if(target==0):
        ans.append(curr.copy())
        return   
    if(target<0 or ind==len(can)):
        return
    curr.append(can[ind])
    generate(ind,curr,ans,can,target-can[ind])  
    curr.pop()  
    generate(ind+1,curr,ans,can,target)  
def combination(can,target):   
    ind=0
    curr=[]
    ans=[]
    generate(ind,curr,ans,can,target)
    return ans
can=list(map(int,input().split()))
target=int(input())
print(combination(can,target))








    