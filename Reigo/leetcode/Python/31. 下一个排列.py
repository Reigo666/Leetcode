from typing import List,Optional

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        lens=len(nums)
        i=lens-1
        for i in range(lens-1,-1,-1):
            if i>=1 and nums[i]>nums[i-1]:
                for j in range(lens-1,i-1,-1):
                    #找到第一个比nums[i-1]大的数
                    if nums[j]>nums[i-1]:
                        #交换数值
                        nums[j],nums[i-1]=nums[i-1],nums[j]
                        break
                break
        #使i到最后一位改为升序
        l=i
        r=lens-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
                        
sol=Solution()
nums1 = [1,2,4,6,5,3]
nums2 = [6,5,4,3,2,1]
sol.nextPermutation(nums2)
print(nums2)
#print(sol.nextPermutation(nums1))


# 输入：nums = [1,2,3]
# 输出：[1,3,2]
