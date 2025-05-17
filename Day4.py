'''
def fun(n):
    if n<=1: return 1
    fun(n-1)
    return n+fun(n-2)
print(fun(5))    
'''

#printing the sum of digits in a number
'''
def fun(n):
    if n==0:
        return 0
    return 1+fun(n//10)
print(fun(1234))
'''
# another method
'''
def fun(n):
    if n//10==0:
        return 1
    return 1+fun(n//10)
print(fun(12))
'''
# printing the sum of the digits in a number by using recursion
'''
def fun(n):
    if n//10==0:
       return n
    return n%10 + fun (n//10)
print(fun(157)) 
'''
# find the minimum number in a list
'''
def fun(nums):
    def rec(nums,i):
        if i == len(nums)-1:
            return nums[i]
        min = rec(nums,i+1)
        return min if min<nums[i] else nums[i]
    return rec(nums,0)
print(fun([5,3,1,9,2]))
'''
# find the maximum number in a list
'''
def fun(nums):
    def rec(nums,i):
        if i == len(nums)-1:
            return nums[i]
        max = rec(nums,i+1)
        return max if max>nums[i] else nums[i]
    return rec(nums,0)
print(fun([5,3,1,9,2]))
'''
# find the min max numbers in a list
'''
def fun(nums):
    def rec(nums,i):
        if i == len(nums)-1:
            return nums[i], nums[i]
        min , max= rec(nums,i+1)
        min = min if min<nums[i] else nums[i]
        max = max if max>nums[i] else nums[i]
        return min, max 
    return rec(nums,0)
min, max = fun([5,3,6,7,8])
print(min,max)
'''
#find the middle value in a list for odd index value using recursion
'''
def mid(n):
    slow=n
    fast=n
    while(fast and fast.next):
        slow=slow.next
        fast=fast.next.next
    return slow.val 
n=list(map(int,input().split(",")))    
print(mid(n))
'''
