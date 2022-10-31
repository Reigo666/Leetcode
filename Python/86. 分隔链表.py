
import collections
from multiprocessing import dummy
from typing import  List,Optional
import copy


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummyhead1=ListNode(0,head)
        dummyhead2=ListNode(0,None)
        pre=dummyhead1
        p=head
        q=dummyhead2
        while p:
            if p.val>=x:
                q.next=p
                q=q.next
                p=p.next
                q.next=None
            else:
                pre.next=p
                pre=pre.next
                p=p.next
            
        pre.next=dummyhead2.next
        return dummyhead1.next

sol=Solution()
#head = [1,4,3,2,5,2]
#[1,4,3,2,5,2]

x = 3

head6=ListNode(2,None)
head5=ListNode(5,head6)
head4=ListNode(2,head5)
head3=ListNode(3,head4)
head2=ListNode(4,head3)
head1=ListNode(1,head2)

head=sol.partition(head1,x)
while head:
    print(head.val)
    head=head.next
#print(sol.partition(head1,x))
# 输入：head = [1,4,3,2,5,2], x = 3
# 输出：[1,2,2,4,3,5]
