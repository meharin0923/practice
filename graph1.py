def graph(v,e,edges):
    adjlist=[]
    for i in range(v):
        adjlist.append([])
    for n,m in edges:     
        adjlist[n].append(m) 
        adjlist[m].append(n) 
    for lst in adjlist:
        lst.sort()
    return adjlist
v=int(input())
e=int(input())
edges=[] 
for i in range(e):
    lst=list(map(int,input().split()))
    edges.append(lst)  
print(graph(v,e,edges))         