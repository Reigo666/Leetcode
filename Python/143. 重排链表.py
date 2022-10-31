
import collections
from typing import  List,Optional
import copy

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    #注意细节
    #翻转时最后的节点next要置空
    #快慢节点分家时，慢节点next最后要置空
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        dummyhead=ListNode(0,head)
        fastp=dummyhead
        slowp=dummyhead
        while fastp and fastp.next:
            slowp=slowp.next
            fastp=fastp.next.next
        reversehead=slowp.next
        if not reversehead:
            return head
        slowp.next=None

        root=dummyhead.next
        while root:
            print(root.val)
            root=root.next

        #reverse
        guardl=ListNode(0,reversehead)
        guardr=reversehead
        insertnode=reversehead.next
        while insertnode:
            nextnode=insertnode.next
            guardl.next=insertnode
            insertnode.next=guardr
            guardr=insertnode
            insertnode=nextnode
        reversehead.next=None

        root=guardl.next
        while root:
            print(root.val)
            root=root.next

        #重组
        cur=dummyhead.next
        insertnode=guardl.next
        while cur and insertnode:
            nextcurnode=cur.next
            nextinsertnode=insertnode.next

            cur.next=insertnode
            insertnode.next=nextcurnode

            cur=nextcurnode
            insertnode=nextinsertnode

        return head
head5=ListNode(5,None)
head4=ListNode(4,head5)
head3=ListNode(3,head4)
head2=ListNode(2,head3)
head1=ListNode(1,head2)
sol=Solution()
root=sol.reorderList(head1)

while root:
    print(root.val)
    root=root.next