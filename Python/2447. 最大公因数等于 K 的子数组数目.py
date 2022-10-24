class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def gcd(a,b):
            t=a%b
            while(t!=0):
                a=b
                b=t
                t=a%b
            return b
        n=len(nums)
        dp=[[0]*n for _ in range(n)]
        ans=0
        for j in range(n):
            for i in range(j,-1,-1):
                if i==j:
                    dp[i][j]=nums[i]
                else:
                    dp[i][j]=gcd(dp[i][j-1],nums[j])
                if dp[i][j]==k:
                    ans+=1
        return ans