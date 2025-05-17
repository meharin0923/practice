def bfs(i,visted,q,adj,ans):
    while(q):
        node=q.pop(0)
        for it in adj[node]:
            if visited[it]==0:
                visited[it]=1
                q.append(it)
        ans.append(node)
def bfs(adj):
    v=len(adj)
    ans=[]
    visited=0*v
    for i in rane(0,v):
        if (visited[i]==0):
            visited[i]=1
            q=[i]
            bfs(i,visited,q,adj)
    return ans
adj=;ist(map(int,(input().split))
print(bfs(adj))
         