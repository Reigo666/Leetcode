class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        nums.sort()
        nums.insert(0,0)

        l=0
        r=len(nums)-1
        def solve(k,l,r):
            while(l<r):
                mid=(l+r)//2
                if nums[mid]-mid<=k-1:
                    l=mid+1
                elif nums[mid]-mid>=k:
                    r=mid
            if nums[l]-l<=k-1:
                l=l+1
            return l
        l1=solve(1,l,r)
        if l1==len(nums):
            return [l1,l1+1]
        l2=solve(2,l1,r)
        if l2==len(nums):
            return [nums[l1]-1,l2+1]
        print(l1,l2)
        if l1!=l2:
            return [nums[l1]-1,nums[l2]-1]
        else:
            return [nums[l1]-2,nums[l2]-1]
            

