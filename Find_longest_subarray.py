'''
arr=list(map(int,input().split())) #T.C:-O(N^2)
k=int(input())
n=len(arr)
maxLen=0
for i in range(0,n):
    for j in range(i,n):
        if(sum(arr[i:j+1])<=k):
            maxLen=max(maxLen,j-i+1)
print(maxLen)
'''
#optimal method
'''
arr=list(map(int,input().split())) #T.C:-O(2N)
k=int(input())
n=len(arr)
maxLen=0
left=0
right=0
Sum=0
while(right<n): #O(N)
    Sum+=arr[right] #expand
    while(Sum>k):# O(N)
        Sum-=arr[left] #shrink
        left+1
    maxLen=max(maxLen,right-left+1)
    right+=1    
print(maxLen)
'''
# Optimal method

arr=list(map(int,input().split())) #T.C:-O(N)
k=int(input())
n=len(arr)
maxLen=0
left=0
right=0
Sum=0
while(right<n): #O(N)
    Sum+=arr[right] #expand
    if(Sum>k):
        Sum-=arr[left] #shrink
        left+1
    maxLen=max(maxLen,right-left+1)
    right+=1
print(maxLen)