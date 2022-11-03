class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        sequence=" "+sequence

        dp=[0]*len(sequence)
        ans=0
        for i in range(1,len(sequence)):
            if i+1-len(word)<=0:
                continue
            if sequence[i+1-len(word):i+1]==word:
                dp[i]=dp[i-len(word)]+1
                ans=max(ans,dp[i])
        return ans
        
            