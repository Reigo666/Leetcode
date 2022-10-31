import collections
from typing import  List,Optional
import copy

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        dict=collections.defaultdict(list)
        p=head
        while p:
            if p in dict[p.val]:
                return p
            dict[p.val].append(p)
            p=p.next
        return None