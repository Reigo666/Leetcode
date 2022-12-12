class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        q=[0]
        nums=[-1]+nums
        i0=0
        i1=0
        ans=0
        for i in range(1,len(nums)):
            if left<=nums[i]<=right:
                i1=i
            elif nums[i]<left:
                pass
            elif nums[i]>right:
                i0=i
                i1=i
            ans+=i1-i0
        return ans


            