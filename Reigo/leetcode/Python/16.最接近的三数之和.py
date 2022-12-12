from typing import List
class Solution:
    #排序+双指针
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans=0 
        lens=len(nums)
        if lens<3: return ans
        nums.sort()
        mindif=abs(nums[0]+nums[1]+nums[2]-target)
        ans=nums[0]+nums[1]+nums[2]
        for i in range(lens):
            if i>0 and nums[i]==nums[i-1]:continue
            l=i+1
            r=lens-1
            while l<r:
                tempdif=nums[i]+nums[l]+nums[r]-target
                if abs(tempdif)<mindif:
                    mindif=abs(tempdif)
                    ans=nums[i]+nums[l]+nums[r]
                if tempdif>0:
                    r-=1
                    continue
                elif tempdif<0:
                    l+=1
                    continue
                else:
                    return target
        return ans
sol=Solution()
nums1 = [-1,2,1,-4]
nums2 = [0,0,0]
nums3=[0,1,2]
target1 = 1
target3=3
print(sol.threeSumClosest(nums3,target3))

