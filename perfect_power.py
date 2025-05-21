'''
def nthRoot(n,m): #T.C:-O(N)
    ans=-1
    for i in range(1,m+1):
        if(i**n==m):
            ans=i
            break
        elif(i**n>m):
            break
    return ans
n=int(input())
m=int(input())
print(nthRoot(n,m))
'''
# another method
'''
def nthRoot(n,m): #T.C:-O(N)
    ans=-1
    for i in range(1,m+1):
        if(i**n==m):
            return i
        elif(i**n>m):
            break
    return ans
n=int(input())
m=int(input())
print(nthRoot(n,m))
'''

#by using binary search
def nthroot(n,m):#T.C:-O(logN)
    ans=-1
    low=0
    high=m
    while(low<=high):
        mid=(low+high)//2
        if(mid**n==m):
            return mid
        elif(mid**n>m):
            high=mid-1
        else:
            low=mid+1
    return -1
n=int(input())
m=int(input())
print(nthroot(n,m))