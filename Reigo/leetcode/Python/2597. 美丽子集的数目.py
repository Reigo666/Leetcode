class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        ans=0
        def backTrack(i,seen):
            if i>=len(nums):
                nonlocal ans
                ans+=1
                return
            needremove=True
            if nums[i] in seen:
                needremove=False
            
            if nums[i]-k not in seen and nums[i]+k not in seen:
                seen.add(nums[i])
                backTrack(i+1,seen)
            else:
                if needremove:
                    needremove=False
            if needremove:
                seen.remove(nums[i])
            backTrack(i+1,seen)
            
            
            
        backTrack(0,set())
        return ans-1