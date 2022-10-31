from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyhead=ListNode(0,None)
        tempnode=dummyhead
        while list1 or list2:
            if not list1:
                tempnode.next=list2
                break
            if not list2:
                tempnode.next=list1
                break
            if list1.val<=list2.val:
                tempnode.next=list1
                list1=list1.next
            else:
                tempnode.next=list2
                list2=list2.next
            tempnode=tempnode.next
        return dummyhead.next
sol=Solution()

l1 = [1,2,4]
l2 = [1,3,4]
ans=sol.mergeTwoLists(l1,l2)
while ans:
    print(ans.val)
    ans=ans.next



#输入：l1 = [1,2,4], l2 = [1,3,4]
#输出：[1,1,2,3,4,4]