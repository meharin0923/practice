# printing binary values of numbers
'''
a = 8
rem="" 
while a:
    rem += str(a%2)
    a = a//2
print(rem[::-1])
'''

# printing binary to decimal
'''
a = "101"
a = a[::-1]
dec = 0
for i in range(len(a)):
    dec += int(a[i])*(2**i)
print(dec)
'''

#printing decimal to binary using bitwise ope
'''
a = 8
rem=""
while a:
    rem += str(a&1)
    a = a>>1
print(rem[::-1])
'''

#printing binary to decimal using bitwise ope
'''
a=input()
dec=0
for i in a:
    dec = (dec<<1) |int(i)
print(dec)
'''

# counting the number of bits using bitwise ope
'''
a = 8
a=8
count=0
while a:
    a=a>>1
    count+=1
print(count)
'''

# count set bits that is count no.of 1's
'''
a = 5
count=0
while a:
    if a&1==1:
        count+=1
    a = a>>1
print(count)
'''
# count set bits that is count no.of 0's
'''
a = 5
count=0
while a:
    if (a&1!=1):
        count+=1
    a = a>>1
print(count)
'''

# another method
'''
a = 100
count=0
while a:
    if (a&1==0):
        count+=1
    a = a>>1
print(count)
'''

# print no.of moves until its get one after and ope
'''
a=4
count=0
while a&1==0:
    a = a>>1
    count+=1
print(count)
'''

#another method
'''
a=4
count=0
while a&1==1:
    a = a<<1
    count+=1
print(count)
'''

# print no.of moves until it gets one by using left shift ope
'''
a = 10
count=0
temp = a
while a:
    a = a>>1
    count+=1
while temp&1==0:
    temp = temp>>1
    count-=1
print(count)
'''
# print index value digit if it is 0 then print 1 and vice versa
'''
def fun(a, i):
    mask=1<<i
    mask = ~mask
    return a&mask
a=int(input())
i=int(input())
print(fun(a,i))
'''

# print index value digit if it is 1 then print 0 and vice versa
'''
def fun(a, i):
    mask=1<<i
    return a|mask
a=int(input())
i=int(input())
print(fun(a,i))
'''

# print binary number index value digit
'''
def fun(a , i):
    mask = 1<<i
    return int(mask&a>0)
a=int(input())
i=int(input())
print(fun(a,i)
'''
#power of 2
'''
def fun(a):
    return a&a-1==0
a=int(input())
print(fun(a))
'''
# print unique value in a list by using bitwise ope
'''
a=input()
res = 0
for i in a:
    res ^=i
print(res)
'''
# count the digits in a number using recursion
'''
def fun(n):
    if n:
        fun(n-1)
        return n
print(fun(5))
'''
#
'''
def fun(n):
    print(n)
    fun(n-1)
print(fun(5)) 
'''
#
def fun(n):
    if n==1: return 1
    fun(n-1)
    fun(n-2)
    print(n)
print(fun(5))    
