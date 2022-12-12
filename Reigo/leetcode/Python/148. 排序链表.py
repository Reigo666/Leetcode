import collections
from typing import  List,Optional
import copy
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p=head
        nums=[]
        while p:
            nums.append(p.val)
            p=p.next
        nums.sort()
        p=head
        i=0
        while p:
            p.val=nums[i]
            i+=1
            p=p.next
        return head