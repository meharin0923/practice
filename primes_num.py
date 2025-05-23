'''
n=int(input())
for i in range(1,n+1):
    if(n%i==0):
        print(i)
'''
#
'''
n=int(input())
c=0
for i in range(1,n+1):
    if(n%i==0):
        print(i)
        c+=1
if(c==2):
        print("prime")
else:
     print("not prime")
'''
#another method
'''
def isprime(num):#T.C:-O(N^2)
    c=0
    for i in range(1,num+1):
        if(num%i==0):
            c+=1
    return c==2
n=int(input())
count=0
for num in range(2,n):
    if(isprime(num)):
        count+=1
print(count)
'''
#another optimal way by seive of erathosthensis method
'''
n=int(input())
prime=[1]*n
for i in range(2,n):
    if(prime[i]==1):
        for j in range(2*i,n,i):
            prime[j]=0
count=0
for i in range(2,n):
    if(prime[i]==1):
        count+=1
print(count)
'''

n=int(input())#T.C:-O(N.LOG(LOGN)) = O(1)
prime=[1]*n
for i in range(2,int(n**0.5)+1):
    if(prime[i]==1):
        for j in range(i*i,n,i):
            prime[j]=0
count=0
for i in range(2,n):#T.C:-O(N)
    if(prime[i]==1):
        count+=1
print(count)
