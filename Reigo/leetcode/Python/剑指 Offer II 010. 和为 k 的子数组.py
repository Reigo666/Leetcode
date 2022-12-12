class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum=[0]
        dict=defaultdict(int)
        dict[0]=1
        ans=0
        for i in range(len(nums)):
            sum1=nums[i]+presum[i]
            presum.append(nums[i]+presum[i])
            if sum1-k in dict:
                ans+=dict[sum1-k]
            dict[sum1]+=1
        return ans