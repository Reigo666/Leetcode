import collections
from typing import  List,Optional
import copy
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        pa=headA
        pb=headB
        
        while pa!=pb:
            if not pa:
                pa=headB
            else:
                pa=pa.next
            if not pb:
                pb=headA
            else:  
                pb=pb.next      
        return pa