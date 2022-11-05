class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right=[0]*(len(nums)+1)
        for i in range(len(nums)-1,-1,-1):
            right[i]=right[i+1]+nums[i]
        left=[0]
        for i in range(len(nums)):
            if left[i]==right[i+1]:
                return i
            left.append(left[i]+nums[i])
        return -1 
        
        
            