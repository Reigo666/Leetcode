# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        
        ans=[0]*len(arr)
        s=[]
        for i in range(len(arr)):
            while s and arr[i]>arr[s[-1]]:
                idx=s.pop()
                ans[idx]=arr[i]
            s.append(i)
        return ans