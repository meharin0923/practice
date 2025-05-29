'''
def reverseList(self, head):
    temp=head
    arr=[]
    while(temp):
        arr.append(temp.val)
        temp=temp.next
    arr=arr[::-1]
    i=0
    temp=head
    while(temp):
        temp.val=arr[i]
        i+=1
        temp=temp.next
    return head  
'''      
    prev=None
    temp=head
    while(temp):
        front=temp.next
        temp.next=prev
        prev=temp
        temp=front
    return prev