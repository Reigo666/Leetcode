from typing import List,Optional



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:return
        lens=len(lists)
        return self.merge(0,lens-1,lists)
    #将左到右的所有链表连接起来,返回结果
    def merge(self,l,r,lists):
        #停止条件
        if l==r:
            return lists[l]
        #分治左右
        mid=l+(r-l)//2
        lnode=self.merge(l,mid,lists)
        rnode=self.merge(mid+1,r,lists)
        ansnode=self.mergeTwoList(lnode,rnode)
        return ansnode
    #mergeTwoList也可以用递归 使l1.next=mergeTwoList(l1.next,l2)
    def mergeTwoList(self,lnode,rnode):
        dummynode=ListNode()
        tempnode=dummynode
        if not lnode:return rnode
        if not rnode:return lnode
        while lnode and rnode:
            if lnode.val<=rnode.val:
                tempnode.next=lnode
                lnode=lnode.next
                tempnode=tempnode.next
            else:
                tempnode.next=rnode
                rnode=rnode.next
                tempnode=tempnode.next
        if not lnode:
            tempnode.next=rnode          
        if not rnode:
            tempnode.next=lnode
        return dummynode.next
sol=Solution()
node1=ListNode(5,None)
node2=ListNode(4,node1)
node3=ListNode(1,node2)

node4=ListNode(4,None)
node5=ListNode(3,node4)
node6=ListNode(1,node5)

node7=ListNode(6,None)
node8=ListNode(2,node7)

lists1 = [node3,node6,node8]
listans=sol.mergeKLists(lists1)
while listans:
    print(listans.val)
    listans=listans.next

# 输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]