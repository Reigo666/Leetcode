# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        list1=[]
        p=head
        while p:
            list1.append(p)
            p=p.next

        l=1
        r=len(list1)-1

        rturn=True

        pre=list1[0]
        #cnt=30
        while l<=r:
            
            if rturn:
                pre.next=list1[r]
                pre=pre.next
                r-=1
                rturn=not rturn
            else:
                pre.next=list1[l]
                pre=pre.next
                l+=1
                rturn=not rturn
        pre.next=None





