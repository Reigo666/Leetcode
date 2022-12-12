from typing import List,Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX=2**31-1
        INT_MIN=-2**31
        if dividend==INT_MIN:
            if divisor==-1:
                return INT_MAX
            if divisor==1:
                return INT_MIN
        
        if dividend==0:
            return 0
        


        #判断Z*Y >= X是否成立
        #快速乘
        def quickAdd(x:int,y:int,z:int):
            res=0
            add=y
            #计算Z*Y等于多少，使用z个Y不断翻倍计算,直到z=1
            #倒叙计算 45->22->11->5->2->1
            #当z为奇数时，/2会导致一个add的丢失
            #45->22的add只丢失了一次,而先前的11->5的add由于后续的翻倍会丢失多次
            #add相当于总共翻了多少次倍，res代表丢失了多少次单数的值，最后的add+res就是总加和值
            while z>0:
                #代表丢失
                if (z&1)==1:
                    if res<x-add:return False
                    res+=add
                if z!=1:
                    #add翻倍,如果翻倍后不等式不成立返回失败
                    if add<x-add:
                        return False
                    add+=add
                z>>=1
            return True              
        #X/Y=Z  X,Y均为负数
        #Z*Y >= X > (Z+1)*Y
        #二分查找Z [1:INT_MAX-1]

        rev=False
        if dividend>0:
            dividend=-dividend
            rev=not rev
        if divisor>0:
            divisor=-divisor
            rev=not rev
        

        l,r=1,INT_MAX
        ans=0
        while l<=r:
            mid=((r-l)>>1)+l
            #Z越小越容易成功,成功时说明z偏小
            if quickAdd(dividend,divisor,mid):
                ans=mid
                if mid==INT_MAX:
                    break
                l=mid+1
            else:
                r=mid-1

        return -ans if rev else ans 


        

sol=Solution()


print(sol.divide(32,5))

# 输入：haystack = "hello", needle = "ll"
# 输出：2


