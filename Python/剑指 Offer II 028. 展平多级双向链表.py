"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':

        def solve(head):
            cur=head
            pre=None
            while cur:
                print(cur.val,cur.next,cur.prev,cur.child)
                if not cur.child:
                    if cur.next==None:
                        pre=cur
                    cur=cur.next
                else:
                    aft=cur.next
                    childnode=cur.child
                    child_lastnode=solve(childnode)
                    #父子前后
                    cur.next=childnode
                    childnode.prev=cur
                    cur.child=None
                    #子最后节点 和 cur下一个节点 前后
                    print("child_lastnode",child_lastnode.val,child_lastnode.next,child_lastnode.prev,child_lastnode.child)
                    if aft!=None:
                        child_lastnode.next=aft
                        aft.prev=child_lastnode
                    elif aft==None:
                        return child_lastnode
                    cur=aft
            return pre
        solve(head)
        return head