# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast=head
        slow=head
        dummyhead=ListNode(-1,head)
        for i in range(n):
            fast=fast.next
        
        pre=dummyhead
        while fast:
            fast=fast.next
            pre=slow
            slow=slow.next
        
        pre.next=slow.next
        del slow
        return dummyhead.next