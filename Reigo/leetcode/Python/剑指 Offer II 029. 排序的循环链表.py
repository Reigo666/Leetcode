import collections
from typing import  List,Optional
import copy
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if head==None:
            head=Node(insertVal,None)
            head.next=head
        else:
            p=head
            q=head.next
            if p!=q:
                while True:
                    if q==head:
                        node=Node(insertVal,q)
                        p.next=node
                        break
                    if q.val>=p.val:
                        if insertVal>=p.val and insertVal<=q.val:
                            node=Node(insertVal,q)
                            p.next=node
                            break
                    else:
                        if (insertVal>=p.val and insertVal>=q.val) or (insertVal<=p.val and insertVal<=q.val):
                            node=Node(insertVal,q)
                            p.next=node
                            break
                    p=p.next
                    q=q.next
            else:
                node=Node(insertVal,q)
                p.next=node
        return head