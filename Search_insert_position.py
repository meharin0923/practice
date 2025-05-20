def searchinsert(nums,tar): #k=target
    n=len(nums)
    low = 0
    high = n-1
    ans = n
    while(low<=high):
        mid=(low+high)//2
        if(nums[mid]>=tar):
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
nums=list(map(int,input().split()))
tar=int(input())
print(searchinsert(nums,tar))

