
import collections
from multiprocessing import dummy
from typing import  List,Optional
import copy

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m-1>=0 and n-1>=0:
            if nums1[m-1]<=nums2[n-1]:
                nums1[m+n-1]=nums2[n-1]
                n-=1
            else:
                nums1[m+n-1]=nums1[m-1]
                m-=1
        while n>=1:
            nums1[n-1]=nums1[n-1]
        return nums1
sol=Solution()

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(sol.merge(nums1,m,nums2,n))




# 输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# 输出：[1,2,2,3,5,6]
# 解释：需要合并 [1,2,3] 和 [2,5,6] 。
# 合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。


