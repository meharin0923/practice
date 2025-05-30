'''
def lengthOfLongestSubstring(s):
    n=len(s)   #T.C:-O(N^2)  #SC:O(1)
    maxLen=0
    for i in range(0,n):
        checker=[0]*256
        for j in range(i,n):
            if(checker[ord(s[j])]==1):
                break
            checker[ord(s[j])]=1
            maxLen=max(maxLen,j-i+1)
        return maxLen
s=input()
print(lengthOfLongestSubstring(s))
'''
#
def lengthOfLongestSubstring(s):
    n=len(s)
    maxLen=0
    left=0
    right=0
    d={}
    while(right<n):
        if(s[right] in d):
            if(d[s[right]]>=left):
                left=d[s[right]]+1
        d[s[right]]=right
        maxLen=max(maxLen,right-left+1)
        right+=1
    return maxLen
s=input()
print(lengthOfLongestSubstring(s))