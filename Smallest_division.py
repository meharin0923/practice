# linear solution
'''
from math import*
def smallestdivisior(arr,k):
    for div in range(1,max(arr)+1):
        Sum=0
        for num in arr:
            Sum+=ceil(num/div)
        if(Sum <=k):
            return div
arr=list(map(int,input().split()))
k=int(input())
print(smallestdivisior(arr,k))
'''
# binary solution
from math import*
def Smallestdivisior(arr,k):
    low=1
    high=max(arr)
    while(low<=high):
        div=(low+high)//2
        Sum=0
        for num in arr:
            Sum+=ceil(num/div)
        if(Sum<=k):
            high=div-1
        else:
            low=div+1
    return low
arr=list(map(int,input().split()))
k=int(input())
print(Smallestdivisior(arr,k))


