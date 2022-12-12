# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        fast=head
        slow=head
        
        while fast:
            fast=fast.next
            if fast:
                fast=fast.next
            else:
                return None
            
            slow=slow.next

            if fast==slow:
                break
        
        if fast==None:
            return None
        
        fast=head
        while fast!=slow:
            fast=fast.next
            slow=slow.next
        
        return slow


