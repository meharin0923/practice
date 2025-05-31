'''
def longestones(nums,k):#1004
    n=len(nums)
    maxLen=0
    for i in range(0,n):
        zero_count=0
        for j in range(i,n):
            if(nums[j]==0):
                zero_count+=1
            if(zero_count>k):
                break
            maxLen=max(maxLen,j-i+1)
    return maxLen
nums=list(map(int,input().split()))
k=int(input())
print(longestones(nums,k))
'''
#optimal code
'''
def longestones(nums,k):
    n=len(nums)
    left=0
    right=0
    maxLen=0
    zero_count=0
    for right in range(n):
        if(nums[right]==0):
            zero_count+=1
        while(zero_count>k):
            if(nums[left]==0):
                zero_count-=1
            left+=1
        maxLen=max(maxLen,right-left+1)
    return maxLen
nums=list(map(int,input().split()))
k=int(input())
print(longestones(nums,k))
'''
#Sliding window method
def longestones(nums,k):
    n=len(nums)
    left=0
    right=0
    maxLen=0
    zero_count=0
    while(right<n):
        if(nums[right]==0):
            zero_count+=1
        if(zero_count>k):
            while(zero_count>k):
                if(nums[left]==0):
                    zero_count-=1
                left+=1
            maxLen=max(maxLen,right-left+1)
        right+=1
    return maxLen
nums=list(map(int,input().split()))
k=int(input())
print(longestones(nums,k))


