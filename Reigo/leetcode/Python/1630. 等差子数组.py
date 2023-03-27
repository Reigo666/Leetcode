class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def solve(ll,rr):
            arr=sorted(nums[ll:rr+1])
            if len(arr)==2:
                return True
            diff=arr[1]-arr[0]
            for i in range(2,len(arr)):
                if diff!=arr[i]-arr[i-1]:
                    return False
            return True
        
        ans=[]
        for e in list(zip(l,r)):
            ans.append(solve(e[0],e[1]))
        
        return ans