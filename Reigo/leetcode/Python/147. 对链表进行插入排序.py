import collections
from typing import  List,Optional
import copy

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummyhead=ListNode(-1,head)
        p=head
        lastsorted=head
        cur=lastsorted.next
        while cur:
            if lastsorted.val<=cur.val:
                lastsorted=lastsorted.next
            else:
                prev=dummyhead
                while prev.next.val<cur.val:
                    prev=prev.next
                
                lastsorted.next=cur.next

                nextnode=prev.next
                prev.next=cur
                cur.next=nextnode

            cur=lastsorted.next
        return dummyhead.next

head5=ListNode(1,None)
head4=ListNode(2,head5)
head3=ListNode(3,head4)
head2=ListNode(4,head3)
head1=ListNode(5,head2)
sol=Solution()
root=sol.insertionSortList(head1)

while root:
    print(root.val)
    root=root.next