def zigzagLevelOrder(self, root):
        if(root==None):
            return []
        q=[root]
        ans=[]
        while(q):
            level=[]
            for i in range(len(q)):
                node=q.pop(0)
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
                level.append(node.val)
            ans.append(level)
        for i in range(len(ans)):
            if(i%2==1):
                ans[i]=ans[i][::-1]
        return ans
