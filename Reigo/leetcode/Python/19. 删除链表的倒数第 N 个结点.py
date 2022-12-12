from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    #双循环垃圾解法
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        tempnode=ListNode()
        tempnode=head
        if tempnode==None:
            return head
        numnode=1

        if tempnode.next==None:
            return None

        if tempnode.next.next==None:
            if n==1:
                tempnode.next=None
                return head
            elif n==2:
                ansnode=tempnode.next
                tempnode.next=None
                return ansnode
        while tempnode.next!=None:
            tempnode=tempnode.next
            numnode+=1
        
        actnum=numnode-n-1
        print(actnum)
        tempnode=head
        for i in range(actnum):
            tempnode=tempnode.next

        if actnum==-1:
            tempnode=head.next
            head.next=None
            return tempnode

        p= tempnode
        q= p.next
        r= q.next

        q.next=None
        p.next=r
        
        return head
    #双指针(好) 写的不好，可以虚构一个头节点，防止头节点最终被删除的特殊情况，最后再输出假头节点dummyhead的下一节点
    def removeNthFromEnd1(self, head: ListNode, n: int) -> ListNode:
        lnode=head
        rnode=head
        flag=0
        for i in range(n+1):
            if rnode.next!=None:
                rnode=rnode.next
            else:
                if i==n-1:
                    flag=2
                elif i==n:
                    flag=1
                break 
        if flag==2:
            tempnode=head.next
            head.next=None
            return tempnode
        if flag==1:
            tempnode=head.next.next
            deletenode=head.next
            deletenode.next=None
            head.next=tempnode
            return head
        
        while rnode.next!=None:
            rnode=rnode.next
            lnode=lnode.next
        lnode=lnode.next
        deletenode=lnode.next
        if deletenode.next==None:
            lnode.next=None
        else:
            lnode.next=deletenode.next
            deletenode.next=None
        return head
sol=Solution()
#head5=ListNode(5,None)
#head4=ListNode(4,head5)
#head3=ListNode(3,head4)
head2=ListNode(2,None)
head1=ListNode(1,head2)

n1 = 2
headans=sol.removeNthFromEnd1(head1,n1)
tempnode=headans
while tempnode.next!=None:
    print(tempnode.val)
    tempnode=tempnode.next
print(tempnode.val)


# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]