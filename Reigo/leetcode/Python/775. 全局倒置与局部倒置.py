class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        maxnum=-1
        for i in range(len(nums)-2):
            cmpnum=nums[i+2]
            maxnum=max(maxnum,nums[i])
            if maxnum>cmpnum:
                return False
        return True