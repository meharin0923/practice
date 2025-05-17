
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
'''
def fun(n):
    if n == 0: 
        return 0
    print(n,end=" ")
    fun(n-1)
    print(n,end=" ")
print(fun(5))
'''
#
'''
def fun(n):
    if n:
        fun(n-1)
        return n
print(fun(5))    
'''
#

def fun(n):
    if n==1: return 1
    fun(n-1)
    fun(n-2)
    print(n)
print(fun(5))    
