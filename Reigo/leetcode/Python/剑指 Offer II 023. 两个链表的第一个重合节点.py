# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        h1=headA
        h2=headB

        while h1!=h2:
            if h1:
                h1=h1.next
            else:
                h1=headB
            
            if h2:
                h2=h2.next
            else:
                h2=headA
        
        return h1