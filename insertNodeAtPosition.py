def insertNodeAtPosition(llist, data, position):
    curr_node=llist
    while position>1 and curr_node.next != None:
        position=position-1
        curr_node=curr_node.next
    new_node=SinglyLinkedListNode(data)
    new_node.next=curr_node.next
    curr_node.next=new_node
    return llist
