def findMergeNode(head1, head2):
    temp1=head1
    temp2=head2
    len1=0
    len2=0
    while temp1!=None:
        len1=len1+1
        temp1=temp1.next
    while temp2!=None:
        len2=len2+1
        temp2=temp2.next
    print(len1)
    print(len2)
    
    while(len1>len2):
        head1=head1.next
        len1=len1-1
    while(len1<len2):
        head2=head2.next
        len2=len2-1
    while(len1>0):
        if head1==head2:
            return head1.data
        head1=head1.next
        head2=head2.next
        len1=len1-1
