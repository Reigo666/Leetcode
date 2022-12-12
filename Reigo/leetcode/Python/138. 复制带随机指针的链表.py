
import collections
from typing import  List,Optional
import copy

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        newhead=Node(head.val,None,None)
        
        newcur=newhead
        cur=head
        pre=cur
        while cur:
            nextcur=cur.next
            cur.next=newcur
            newcur.next=nextcur
            if nextcur:
                newcur=Node(nextcur.val,None,None)
            cur=nextcur
        
        cur=head
        newcur=newhead
        while cur:
            if not cur.random:
                newcur.random=None
            else:
                newcur.random=cur.random.next
            cur=newcur.next
            if cur:
                newcur=cur.next  
        cur=head
        newcur=newhead
        while cur:
            nextcur=newcur.next
            cur.next=nextcur
            if nextcur:
                newcur.next=nextcur.next
            else:
                newcur.next=None
            cur=nextcur
            if nextcur:
                newcur=nextcur.next
        return newhead
sol=Solution()
n=5
print(sol.generate(n))




# 输入：s = "babgbag", t = "bag"
# 输出：5


