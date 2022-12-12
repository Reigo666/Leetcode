# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, headA: ListNode, headB: ListNode) -> ListNode:
        l1=[]
        l2=[]
        while headA:
            l1.append(headA.val)
            headA=headA.next
        
        while headB:
            l2.append(headB.val)
            headB=headB.next
        
        l1=l1[::-1]
        l2=l2[::-1]

        if len(l1)<len(l2):
            l1,l2=l2,l1
        l2=l2+[0]*(len(l1)-len(l2))
        

        print(l1,l2)
        dummyhead=ListNode(-1)
        pre=dummyhead
        carry=False
        l3=[]
        for i in range(len(l1)):
            val=l1[i]+l2[i]
            if carry:
                val+=1
                carry=False
            if val>=10:
                val-=10
                carry=True
            l3.append(val)

        print(l3)
        if carry:
            l3.append(1)

        l3=l3[::-1]

        for i in range(len(l3)):
            newnode=ListNode(l3[i])
            pre.next=newnode
            pre=newnode
        return dummyhead.next
        

        
