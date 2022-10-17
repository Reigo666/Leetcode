class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        l=nums[0]
        r=max(nums)
        def check(mid):
            have=0
            for num in nums:
                if num<mid:
                    have+=mid-num
                else:
                    have-=num-mid
                    if have<0:
                        return False
            return True
        while(l<r):
            mid=(l+r)//2
            if check(mid):
                r=mid
            else:
                l=mid+1
        return l