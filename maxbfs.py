def max(root):
    if(root=None):
        return 0
    q=[root]
    c=0
    while(q):
        for i in range(len(q)):
            node=q.pop(0)
            if(node.left):
                q.append(node.left)
            if(node.right):
                q.append(node.right)
        c+=1
    return c
root=list(map,int(input().split()))
print(max(root))