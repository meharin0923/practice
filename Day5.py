# Two sum
'''
def twoSum(nums,target):
    n=len(nums)
    for i in range(0,n):
        for j in range(i+1,n):
            if(nums[i]+nums[j]==target):
                return[i,j]
nums=list(map(int,input().split()))
target=int(input())
twoSum(nums,target)
'''
#another method using dictionary
'''
def twoSum(nums,target):
    d={}
    n=len(nums)
    for a in range(0,n):#T.C:-O(N)
        b=target-nums[a]
        if(b in d):
            return[a,d[b]]
        else:
            d[nums[a]]=a
nums=list(map(int,input().split()))
target=int(input())
twoSum(nums,target)
'''
#another optimal way with using pointers
'''
def twoSum(nums,target):
    n=len(nums)
    low=0 #T.C:-O(log N)
    high=n-1
    while(low<high):
        Sum=nums[low]+nums[high]
        if(Sum==target):
            return "yes"
        elif(Sum>target):
            high-=1
        elif(Sum<target):
            low+=1
    return "No" 
nums=list(map(int,input().split()))
target=int(input())
print(twoSum(nums,target))
'''
 # Three sum
'''
def threeSum(nums,target):
        triplet_sum=set()
        n=len(nums) #T.C: O(N^3)
        for i in range(0,n-2): # 0,3
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    if(nums[i]+nums[j]+nums[k]==0):
                        temp=[nums[i],nums[j],nums[k]]
                        temp.sort()
                        triplet_sum.add(tuple(temp))
        ans=[]
        for triplet in triplet_sum:
             ans.append(list(triplet)) 
        return ans                       
nums=list(map(int,input().split()))
target=int(input())
print(threeSum(nums,target))
'''
#another method using hasing method with a dictionary
'''
def threeSum(nums,target):
    triplet_Sum=set()
    n=len(nums)
    for i in range(0,n-1):
        hashmap=[]
        for j in range(i+1,n):
            k=-(nums[i]+nums[j])
            if(k in hashmap):
                temp=[nums[i],nums[j],k]
                temp.sort()
                triplet_Sum.append(tuple(temp))    
            hashmap.append(nums[j])
    ans=[]
    for triplet in triplet_Sum:
       ans.append(list(triplet))
    return ans
nums=list(map(int,input().split()))
target=int(input())
print(threeSum(nums,target))
'''
#another optimal way with using  two pointers
'''
def threeSum(nums,target):
    nums.sort()
    n=len(nums)
    ans=[]
    for i in range(0,n):
        if(i>0 and nums[i]==nums[i-1]):
          continue
        j=i+1
        k=n-1
        while(j<k):
            Sum=nums[i]+nums[j]+nums[k]
            if(Sum<0):
               j+=1
            elif(Sum>0):
               k -=1
            else:
               temp=[nums[i],nums[j],nums[k]]   
               ans.append(temp)
               j+=1
               k-=1
            while(j<k and nums[j-1]==nums[j]):
               j+=1
            while(j<k and nums[k+1==nums[j]]):
               k-=1
    return ans
nums=list(map(int,input().split()))
target=int(input())
print(threeSum(nums,target))
'''
#Majority element in a list
'''
def majorityElement(nums): 
        n=len(nums)
        for i in nums:
            if(nums.count(i)>n//2):
                return i
nums=list(map(int, input().split(",")))
print(majorityElement(nums))            
'''
#another way using dictinory
'''
def majorityElement(nums):
    d={}
    n=len(nums)
    for i in nums:
        if(i in d):
            d[i]=d[i]+1
        else:
            d[i]=1
    for key,values in d.items():
        if(values>n//2):
            return key
nums=list(map(int, input().split(",")))
print(majorityElement(nums))             
'''

#Majority element 2 in a list
'''
def majorityElement(nums):
        n=len(nums)
        ans=[]
        for i in set(nums):
            if(nums.count(i)>n//3):
                ans.append(i)
        return ans
nums=list(map(int, input().split(",")))
print(majorityElement(nums)) 
'''
#another way using dictinory
'''
def majorityElement(nums):
    d={}
    n=len(nums)
    for i in nums:
        if(i in d):
            d[i]=d[i]+1
        else:
            d[i]=1
    ans=[]        
    for key,values in d.items():
        if(values>n//3):
            ans.append(key)
    return ans
nums=list(map(int, input().split(",")))
print(majorityElement(nums)) 
'''
#SPACE COMPLEXITY
#list,set,dict,tupl = O(N)
#matrix n=O(N^2)
#no extra space = O(1)

                

         
             


