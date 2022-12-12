"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        newnode=Node(insertVal)
        if not head:
            newnode.next=newnode
            return newnode
        
        p=head
        while p.next!=head:
            if p.val>p.next.val:
                if insertVal>=p.val or insertVal<=p.next.val:
                    break

            if insertVal>=p.val and insertVal<=p.next.val:
                break
            p=p.next

        newnode.next=p.next
        p.next=newnode
        return head



