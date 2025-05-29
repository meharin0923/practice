def findheight(root):
            if(root==None):
                return 0
            lh=findheight(root.left)
            rh=findheight(root.right)
            return 1+max(lh,rh)
        return findheight(root)
        