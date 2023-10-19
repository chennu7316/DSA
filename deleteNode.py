def deleteNode(llist, position):
    # Write your code here
    if(position==0):
        return llist.next
    temp=llist
    while position>1 and temp.next!=None:
        temp=temp.next
        position=position-1
    temp.next=temp.next.next
    if list==None:
        return null
    else:
        return llist
