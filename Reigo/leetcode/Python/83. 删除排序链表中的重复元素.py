
import collections
from typing import  List,Optional
import copy

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head==None:
            return None
        pre=head
        cur=head
        while cur:
            if cur.next:
                if cur.next.val!=cur.val:
                    pre=pre.next
                else:
                    while cur.next and cur.next.val==cur.val:
                        cur=cur.next
                    pre.next=cur.next
                    pre=cur.next

            cur=cur.next
        return head






sol=Solution()



head7=ListNode(5,None)
head6=ListNode(4,head7)
head5=ListNode(4,head6)
head4=ListNode(3,head5)
head3=ListNode(3,head4)
head2=ListNode(2,head3)
head1=ListNode(1,head2)
head1=sol.deleteDuplicates(head1)

while head1:
    print(head1.val)
    head1=head1.next
#print(sol.deleteDuplicates(head1))


# 输入：head = [1,1,2,3,3]
# 输出：[1,2,3]


# 输入：head = [1,2,3,3,4,4,5]
# 输出：[1,2,5]
