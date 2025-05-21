#linear solution
'''
from math import*
def kokoeat(arr,k):
    for noOFBanana in range(1,max(arr)+1):
        time=0
        for num in arr:
            time+=ceil(num/noOFBanana)
        if(time<=k):
            return noOFBanana
arr=list(map(int,input().split()))
k=int(input())
print(kokoeat(arr,k))
'''
#binary solution
from math import*
def kokoeat(arr,k):
    low=1
    high=max(arr)
    while(low<=high):
        noOFBanana=(low+high)//2
        time=0
        for num in arr:
            time+=ceil(num/noOFBanana)
        if(time<=k):
            high=noOFBanana-1
        else:
            low=noOFBanana+1
    return low
arr=list(map(int,input().split()))
k=int(input())
print(kokoeat(arr,k))


