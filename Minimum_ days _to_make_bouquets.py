#linear solution
'''
def minDayBloom(m,k,arr):
    if(m>len(arr)):
        return -1
    Min=min(arr)
    Max=max(arr)
    for bloomday in range(Min,Max+1):
        count=0
        noOfB=0
        for flower in arr:
            if(flower<=bloomday):
                count+=1
            else:
                noOfB+=count//k
                count=0
        noOfB+=count//k
        if(noOfB>=m):
            return bloomday
m=int(input())
k=int(input())
arr=list(map(int,input().split()))
print(minDayBloom(m,k,arr))
'''
# binary solution 

