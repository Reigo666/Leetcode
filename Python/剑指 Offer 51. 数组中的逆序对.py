from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ans=0
        def solve(l,r):
            #print(nums,l,r)
            nonlocal ans
            if l>r:
                return
            if l==r:
                return 
            if r-l==1:
                if nums[l]>nums[r]:
                    ans+=1
                    nums[l],nums[r]=nums[r],nums[l]
                return

            mid=(l+r)//2
            solve(l,mid)
            solve(mid+1,r)

            lptr=l
            rptr=mid+1
            while lptr<=mid and rptr<=r:
                if nums[lptr]>nums[rptr]:
                    while rptr<=r and nums[lptr]>nums[rptr]:
                        rptr+=1  
                elif nums[lptr]<=nums[rptr]:
                    ans+=rptr-(mid+1)
                    lptr+=1
            if rptr==r+1:
                while lptr<=mid:
                    ans+=rptr-(mid+1)
                    lptr+=1
            
            temp=sorted(nums[l:r+1])
            nums[l:r+1]=temp
        solve(0,len(nums)-1)
        #print(nums)
        return ans

sol=Solution()
nums=[1,3,2,3,1]
print(sol.reversePairs(nums))