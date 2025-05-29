n=int(input())
m=int(input())
mat=[]
for i in range(n):
    temp=list(map(int,input().split()))
mat.append(temp)
sum=0
for i in range(n):
    for j in range(m):
        if(i==j):
            sum+=mat[i][j]
print(sum)    