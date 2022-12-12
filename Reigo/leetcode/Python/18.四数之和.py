from typing import List
class Solution:
    #排序+双指针
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        lens=len(nums)
        if lens<=3:
            return ans
        nums.sort()

        #i,j去重
        for i in range(lens-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,lens-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                l=j+1
                r=lens-1
                while l<r:
                    tempval=nums[i]+nums[j]+nums[l]+nums[r]
                    if tempval<target:
                        l+=1
                    elif tempval>target:
                        r-=1
                    else:
                        ans.append([nums[i],nums[j],nums[l],nums[r]])
                        while l<r and nums[l]==nums[l+1]:l+=1
                        while l<r and nums[r]==nums[r-1]:r-=1
                        l+=1
                        r-=1              
        return ans

sol=Solution()
nums1 = [1,0,-1,0,-2,2]
target1 = 0
print(sol.fourSum(nums1,target1))

#输入：nums = [1,0,-1,0,-2,2], target = 0
#输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]