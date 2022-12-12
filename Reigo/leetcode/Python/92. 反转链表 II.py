
import collections
from typing import  List,Optional
import copy

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    #守卫法(前插法)
    #反转序列法
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left==right:
            return head
        dummyhead=ListNode(0,head)
        cur=head
        pre=dummyhead
        i=1
        while cur:
            if i==left:
                end=cur
                begin=cur.next
                cur1=cur.next
                cur2=cur.next.next
                for i in range(right-left):
                    cur1.next=cur
                    begin=cur1
                 
                    cur=cur1
                    cur1=cur2
                    if cur2:
                        cur2=cur2.next
     
                pre.next=begin
                end.next=cur1
                return dummyhead.next
            i+=1
            pre=cur
            cur=cur.next
        return dummyhead.next

sol=Solution()
node1=ListNode(5,None)
node2=ListNode(4,node1)
node3=ListNode(3,node2)
node4=ListNode(2,node3)
node5=ListNode(1,node4)

nodenow=sol.reverseBetween(node5,2,4)
while nodenow:
    print(nodenow.val)
    nodenow=nodenow.next