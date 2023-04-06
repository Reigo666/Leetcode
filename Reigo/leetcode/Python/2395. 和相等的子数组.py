class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        seen=set()
        pre=nums[0]
        for i in range(1,len(nums)):
            pre+=nums[i]
            if pre in seen:
                return True
            seen.add(pre)
            pre-=nums[i-1]
        return False