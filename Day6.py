#power of x
'''
def pow(x,n):
    if n<0:
        x=1/x
    n=abs(n)
    ans=1
    for i in range(n):
        ans=ans*x
    return ans
x=int(input())
n=int(input())
print(pow(x,n))
'''
#Another method
'''
def power(x,n):
    if(n==0):
        return 1
    if(n%2==1):
        return x*power(x,n-1)
    return power(x*x,n//2)
def pow(x,n):
    if(n<0):
        x=1/x
    n=abs(n)
    return power(x,n)
x=int(input())
n=int(input())
print(power(x,n))
'''
#subsets
'''
def generate(ind,curr_arr,ans,nums):
    if(ind==len(nums)):
        ans.append(curr_arr.copy())
        return
    curr_arr.append(nums[ind])
    generate(ind+1,curr_arr,ans,nums)
    curr_arr.pop()
    generate(ind+1,curr_arr,ans,nums)
def subsets(nums):
    ind=0
    curr_arr=[]
    ans=[]
    generate(ind,curr_arr,ans,nums)
    return ans
nums=list(map(int,input().split()))
print(subsets(nums))
'''
#check subsequence sum
'''
def check(ind,arr,k):
    if(k==0):
        return True
    if(k<0 or ind==len(arr)):
        return False
    path1=check(ind+1,arr,k-arr[ind])
    if(path1==True):
        return True
    path2=check(ind+1,arr,k)
    return path1 or path2
def checkSubsequenceSum(N,arr,k):
    ind=0
    return check(ind,arr,k)
N = int(input())
arr = list(map(int, input().split()))
k = int(input())
print(checkSubsequenceSum(N,arr,k))
'''

#combination_sum_1
'''
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
'''

#combination_sum_2
'''
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
'''
