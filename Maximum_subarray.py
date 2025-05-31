#
'''
def subarray(nums):
    n=len(nums)
    maxSum=float("-inf")
    for i in range(0,n):
        for j in range(i,n):
            Sum=sum(nums[i:j+1])
            maxSum=max(maxSum,Sum)
    return maxSum
nums=list(map(int,input().split(",")))
print(subarray(nums))
'''
#
def maxSubArray(nums):
    n=len(nums)
    maxLen=0
    maxSum=float("-inf")
    currSum=0
    for i in nums:
        currSum+=i
        maxSum=max(maxSum,currSum)
        if(currSum<0):
            currSum=0
    return maxSum
nums=list(map(int,input().split(",")))
print(maxSubArray(nums))      