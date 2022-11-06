class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l=0
        r=0
        n=len(nums)
        sum1=0
        seen=set()
        ans=0
        while l<n and r<n:
            while nums[r] in seen:
                seen.remove(nums[l])
                sum1-=nums[l]
                l+=1
            seen.add(nums[r])
            sum1+=nums[r]
            r+=1

            while r-l>k:
                seen.remove(nums[l])
                sum1-=nums[l]
                l+=1
            
            if r-l==k:
                ans=max(ans,sum1)
        
        return ans

