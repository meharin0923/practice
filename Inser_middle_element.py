'''
class Solution:
    def insertInMiddle(self, head, x):
        if(head==None):
            return Node(x)
        len=0
        temp=head
        while(temp):
            len+=1
            temp=temp.next
        if(len%2==0):
            prev=None
            slow=head
            fast=head
            while(fast and fast.next):
                prev=slow
                slow=slow.next
                fast=fast.next.next
            newNode=Node(x)
            prev.next=newNode
            newNode.next=slow
            return head
        else:
            slow=head
            fast=head
            while(fast and fast.next):
                slow=slow.next
                fast=fast.next.next
            front=slow.next
            newNode=Node(x)
            slow.next=newNode
            newNode.next=front
            return head
           ''' 
def insertmiddle (head,x):
    if (head==None):
        return Node
    slow=head
    fast=head
    while(fast.next and fast.next.next):
        slow=slow.next
        fast=fast.next.next
    newNode=Node(x)
    front=slow.next
    slow.next=newNode
    newNOde.next=ftront
            
            
            
    
    
        