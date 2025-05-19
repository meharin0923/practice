# BUBBLE SORT : push the max elements to the last by adjacent  swapping
'''
def bubble(arr):
    n=len(arr)
    for i in range(n-1,-1,-1):
        for j in range(i):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=list(map(int,input().split()))
print(bubble(arr))            
'''

#another method
'''
def bubble(arr):
    arr.sort()
    return arr
arr=list(map(int,input().split()))
print(bubble(arr))    
'''
