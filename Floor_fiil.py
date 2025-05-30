def dfs(self,sr,sc,image,visited,n,m,color,ele):
        visited[sr][sc]=1
        image[sr][sc]=color
        for row,col in [[-1,0],[1,0],[0,-1],[0,1]]:
                
            delRow=sr+row
            delCol=sc+col
            if (0 <= delRow < n and 0 <= delCol < m and
                not visited[delRow][delCol] and image[delRow][delCol] == ele):
                self.dfs(delRow, delCol, image, visited, n, m, color,ele)
                
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n=len(image)
        m=len(image[0])
        visited=[]
        for i in range(n):
            temp=[0]*m
            visited.append(temp)
        ele=image[sr][sc]
        if(ele!=color):
            self.dfs(sr,sc,image,visited,n,m,color,ele)
        return image