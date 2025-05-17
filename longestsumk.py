
#by using hasing tecnique
def long(arr,k):
    n=len(arr)
    ans=[]
    for i in range(0,n):
        for j in range(i,n):
            ans.append(arr[i:j+1])
    maxlen=0
    for lst in ans:
        if(sum(lst)==k):
            if(len(lst)>maxlen):
                maxlen=len(lst)
    return maxlen
arr=list(map(int,input().split()))
k=int(input())
print(long(arr,k))                    
    