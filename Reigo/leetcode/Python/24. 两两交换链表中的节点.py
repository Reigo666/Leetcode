from multiprocessing import dummy
from typing import List,Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    #创建虚拟节点 涉及三个节点变动
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return
        dummynode=ListNode()
        dummynode.next=head
        p=head
        q=p.next
        lastnode=dummynode
        while p and q:
            lastnode.next=q
            p.next=q.next
            q.next=p

            lastnode=p
            p=p.next
            if p:
                q=p.next    
        return dummynode.next
    
sol=Solution()

n1 = 3
print(sol.swapPairs(n1))



# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
