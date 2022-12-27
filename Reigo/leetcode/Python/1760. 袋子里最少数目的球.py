class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        nums.sort()

        def check(x):
            idx=bisect.bisect_right(nums,x)
            if nums[idx]==x:
                idx+=1
            t=maxOperations
            for i in range(idx,len(nums)):
                t-=(nums[i]-1)//x
                #print(t,nums[idx])
                if t<0:
                    return False
            return True
            #1,2,3 0
            #4,5,6 1
            #7,8,9 2
        
        l=1
        r=nums[-1]

        while l<r:
            mid=(l+r)//2
            #print(l,r,mid)
            if check(mid):
                r=mid
            else:
                l=mid+1
        #print(check(1))
        return l