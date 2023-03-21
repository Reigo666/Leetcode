class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        #[1,2,2,3]
        #[2,3]
        nums.sort()
        r=1
        ans=0
        l=0
        while r<len(nums):
            while r<len(nums) and nums[r]<=nums[l]:
                r+=1
            
            if r<len(nums):
                ans+=1
            #print(l,r)
            l+=1
            r+=1
        
        return ans