class Solution:
    def findScore(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i]=[nums[i],i]
        
        nums.sort()
        vis=[False]*len(nums)
        
        ans=0
        for i in range(len(nums)):
            if vis[nums[i][1]]:
                continue
            if nums[i][1]-1>=0:
                vis[nums[i][1]-1]=True
            vis[nums[i][1]]=True
            
            if nums[i][1]+1<len(nums):
                vis[nums[i][1]+1]=True
            ans+=nums[i][0]
            #print(vis)
        return ans