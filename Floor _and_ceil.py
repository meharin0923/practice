# FLOOR: largest element in the array such that arr[ind]<=x
# CEIL:  smallest element in the array such that arr[ind]>=x
def Floor_and_Ceil(a,n,x):
    def getFloor(a,n,x):
        low=0
        high=n-1
        ans=-1
        while(low<=high):
            mid=(low+high)//2
            if(a[mid]<=x):
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans
    def getCeil(a,n,x):
        low=0
        high=n-1
        ans=-1
        while(low<=high):
            mid=(low+high)//2
            if(a[mid]>=x):
                ans=a[mid]
                high=mid-1
            else:
                low=mid+1
        return ans
    Floor=getFloor(a,n,x)
    Ceil=getCeil(a,n,x)
    return[Floor,Ceil]
a=list(map(int,input().split()))
n=len(a)
x=int(input())
print(Floor_and_Ceil(a,n,x))

            
            


