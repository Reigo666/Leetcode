class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        r=len(arr)-1
        while r-1>=0 and arr[r]>=arr[r-1]:
            r-=1
        
        ans=r
        for i in range(len(arr)):
            if i>=1:
                if arr[i]<arr[i-1]:
                    break
            while r<len(arr) and arr[r]<arr[i]:
                r+=1
            if r==i:
                return 0
            ans=min(ans,r-i-1)
        return ans

