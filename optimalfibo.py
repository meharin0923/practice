def fib(n):
    prev2=0
    prev1=1
    for i in range(2,n+1):
        curr=prev2+prev1
        prev2=prev1
        prev1=curr
    return prev1
n=int(input())
print(fib(n))