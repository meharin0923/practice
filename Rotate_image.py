def rotate(matrix):
    n=len(matrix)
    m=len(matrix[0])
    dupMat=[]
    for i in range(0,n):
        temp=[0]*n
        dupMat.append(temp)
    for i in range(0,n):
            for j in range(0,n):
                dupMat[j][n-i-1]=matrix[i][j]
    for i in range(0,n):
        for j in range(0,n):
            matrix[i][j]=dupMat[i][j]


#optimal code
def rotate(matrix):
    n=len(matrix)
    for i in range(n-1):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    for i in range(n):
        matrix[i]=matrix[i][::-1]

        
            