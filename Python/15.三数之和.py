from typing import List
class Solution:
    #排序+双指针
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        print(nums)
        lens=len(nums)
        if lens<3:
            return ans
        for i in range(lens):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            addval=-nums[i]
            l=i+1
            r=lens-1
            if l>=r:
                break
            while l<r:
                if nums[l]+nums[r]<addval:
                    l+=1
                    continue
                elif nums[l]+nums[r]>addval:
                    r-=1
                    continue
                elif nums[l]+nums[r]==addval:
                    ans.append([nums[i],nums[l],nums[r]])
                    #去重
                    while l+1<lens and nums[l]==nums[l+1] : l+=1
                    while r-1>i and nums[r]==nums[r-1] : r-=1
                    l+=1
                    r-=1
        return ans
sol=Solution()
nums1 = [-1,0,1,2,-1,-4]
nums2 = []
nums3 = [0]
print(sol.threeSum(nums1))
