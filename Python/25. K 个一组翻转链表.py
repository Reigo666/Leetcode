from typing import List,Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    #递归完成
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:return
        dummynode=ListNode()
        dummynode.next=head
        tempnode=head
        pre=dummynode
        #From start to end做旋转
        while tempnode:
            start=tempnode
            for i in range(k-1):
                tempnode=tempnode.next
                #没有足够节点，返回
                if not tempnode:
                    return dummynode.next
            end=tempnode
            tempnode=tempnode.next
            end.next=None
            pre.next=self.reverse(start)
            pre=start
            start.next=tempnode
        return dummynode.next
    #交换k个节点,返回头节点
    def reverse(self,lnode):
        p=lnode
        q=p.next
        while q:
            nextnode=q.next
            q.next=p
            p=q
            q=nextnode
        return p
       


    
sol=Solution()
node1=ListNode(5,None)
node2=ListNode(4,node1)
node3=ListNode(3,node2)
node4=ListNode(2,node3)
node5=ListNode(1,node4)
k1=3
listans=sol.reverseKGroup(node5,k1)
while listans:
    print(listans.val)
    listans=listans.next


# 输入：head = [1,2,3,4,5], k = 2
# 输出：[2,1,4,3,5]
