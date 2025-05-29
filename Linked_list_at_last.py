newNode=Node(x)
        if(head==None):
            return newNode
        temp=head
        while(temp.next):
            temp=temp.next
        temp.next=newNode
        return head