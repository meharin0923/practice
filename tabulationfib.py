def fib(n,dp):
    if(n==0 or n==1):
        return n
    dp[0]=1
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[-2]
    return dp[n]
n=int(input())
dp=[-1]*(n+1)
print(fib(n,dp))