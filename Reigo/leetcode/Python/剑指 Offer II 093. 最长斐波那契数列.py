class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        dict={}
        for i in range(len(arr)):
            dict[arr[i]]=i
        
        n=len(arr)
        dp=[[0]*n for _ in range(n)]
        ans=0
        for i in range(n):
            for j in range(i-1,-1,-1):
                if arr[i]-arr[j] in dict:
                    k=dict[arr[i]-arr[j]]
                    if k>=j:
                        continue
                    dp[j][i]=max(dp[k][j]+1,3)
                    ans=max(ans,dp[j][i])
        #print(dp)
        return ans

        
