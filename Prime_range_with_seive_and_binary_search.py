import math
import bisect
def sieve(limit):
    prime=[1]*(limit+1)
    prime[0]=prime[1]=0
    for i in range(2,int(limit**0.5)+1):
        if prime[i]:
            for j in range(i*i,limit+1,i):
                prime[j]=0
    return [i for i in range(2,limit+1)if prime[i]]
def is_prime(num,base_primes):
    if num<2:
        return False
    for p in base_primes:
        if p*p>num:
            break
        if num%p==0:
            return False
    return True
L,R=map(int,input().split())
base_primes=sieve(int(math.sqrt(R))+1)
result=[]
for num in range(L,R+1):
    if is_prime(num,base_primes):
        result.append(str(num))
print(" ".join(result))