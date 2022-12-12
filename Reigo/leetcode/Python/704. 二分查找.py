class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bisect_search(nums,target):
            l=0
            r=len(nums)-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
                #print(l,r)
            return -1
        return bisect_search(nums,target)