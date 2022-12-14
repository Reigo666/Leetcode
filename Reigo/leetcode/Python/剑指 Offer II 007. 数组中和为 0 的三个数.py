class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        print(nums)
        for i in range(len(nums)-2):
            if i>=1:
                if nums[i]==nums[i-1]:
                    continue
            l=i+1
            r=len(nums)-1
            target=-nums[i]
            while l<r:
                if nums[l]+nums[r]<target:
                    l+=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                elif nums[l]+nums[r]==target:
                    ans.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
                else:
                    r-=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
        return ans