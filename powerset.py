'''
def power(x,n):
    if(n==0):
        return
    if(n%2==1):
        return x*power(x,n-1)
    return power(x*n,n//2)
def getpower(x,n):
    if(n<0):
        x=i/x
        n=abs(n)
    return getpower(x,n)
n=int(input())
print(power(x,n))    
'''
#another method
def pow(n):
    for i in range(31):
        if(2**i==n):
            return True
    return False
n=int(input())
print(pow(n))    
