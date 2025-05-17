def findnumber(nums):
    c=0
    for i in nums:
        x=len(str(i))
        if(x%2==0):
            c+=1
    return c
nums=str(input())
print(findnumber(nums))