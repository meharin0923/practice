def depthFirstSearch(self,Node,visited,adj,ans):
        visited[Node]=1
        ans.append(Node)
        for i in adj[Node]:
            if(visited[i]==0):
                self.depthFirstSearch(i,visited,adj,ans)
                
    def dfs(self, adj):
        v=len(adj)
        visited=[0]*v
        ans=[]
        Node=0
        if(visited[Node]==0):
            self.depthFirstSearch(Node,visited,adj,ans)
        return ans