
import collections
from typing import  List,Optional
import copy

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n=0
        p=head
        tail=head
        while p:
            n+=1
            tail=p
            p=p.next
        k=k%n
        if not k:return head
        k=n-k-1
        p=head
        for i in range(k):
            p=p.next
        newhead=p.next
        p.next=None
        tail.next=head
        return newhead



sol=Solution()
node1=ListNode(5,None)
node2=ListNode(4,node1)
node3=ListNode(3,node2)
node4=ListNode(2,node3)
node5=ListNode(1,node4)
k=2
nodenow=sol.rotateRight(node5,6)
while nodenow:
    print(nodenow.val)
    nodenow=nodenow.next




# 输入：head = [1,2,3,4,5], k = 2
# 输出：[4,5,1,2,3]





