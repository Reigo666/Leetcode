class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def bisect_left(nums,target):
            l=0
            r=len(nums)
            while l<r:
                mid=(l+r)//2
                if nums[mid]<target:
                    l=mid+1
                else:
                    r=mid
            return l
        return bisect_left(nums,target)