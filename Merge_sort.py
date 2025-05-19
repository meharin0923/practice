# By using two pointers

nums1=list(map(int,input().split()))
nums2=list(map(int,input().split()))
i=0
j=0
result=[]
while(i<len(nums1) and j<len(nums2)):
    if(nums1[i]<=nums2[j]):
        result.append(nums1[i])
        i+=1
    else:
        result.append(nums2[j])
        j+=1   
print(result)


# By using funtion
'''
def ms(nums, n):
    def mergeSort(nums,low,high):
        if(low>=high):
            return
        mid=(low+high)//2
        mergeSort(nums,low,mid)
        mergeSort(nums,mid+1,high)
        Sort(nums,low,mid,high)
    def Sort(nums,low,mid,high):
        i=low
        j=mid+1
        k=[]
        while(i<=mid and j<=high):
            if(nums[i]<=nums[j]):
                k.append(nums[i])
                i+=1
            else:
                k.append(nums[j])
                j+=1
        while(i<=mid):
            k.append(nums[i])
            i+=1
        while(j<=mid):
            k.append(nums[j])
            j+=1
        for ind,val in enumerate(k):
            nums[ind+low]=val
    n=len(nums)
    low=0
    high=n-1
    mergeSort(nums,low,high)
    return nums
nums=list(map(int,input().split()))
n=len(nums)
print(ms(nums, n))
'''


