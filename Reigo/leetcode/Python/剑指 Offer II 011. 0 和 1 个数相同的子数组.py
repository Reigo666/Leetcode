class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dict={}
        dict[0]=0

        presum=0
        ans=0
        for i in range(len(nums)):
            if nums[i]==1:
                presum+=1
            else:
                presum-=1
            if presum not in dict:
                dict[presum]=i+1
            else:
                ans=max(ans,i+1-dict[presum])
        return ans