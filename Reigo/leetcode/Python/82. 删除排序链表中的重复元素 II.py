
import collections
from typing import  List,Optional
import copy

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def deleteDuplicates1(self, head: ListNode) -> ListNode:
        if head==None:
            return None
        dummyhead=ListNode(0,head)
        pre=dummyhead
        cur=head
        while cur:
            if cur.next:
                if cur.val!=cur.next.val:
                    pre=pre.next
                else:
                    while cur.next and cur.val==cur.next.val:
                        cur=cur.next
                    pre.next=cur.next
            else:
                return dummyhead.next
            cur=cur.next                       
        return dummyhead.next
    #递归
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head==None:
            return None
        if head.next:
            if head.next.val==head.val:
                while head.next and head.next.val==head.val:
                    head=head.next
                head=head.next
                return self.deleteDuplicates(head)
            else:
                head.next=self.deleteDuplicates(head.next)
                return head
        else:
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





# 输入：head = [1,2,3,3,4,4,5]
# 输出：[1,2,5]
