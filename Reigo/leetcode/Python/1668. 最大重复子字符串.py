class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n=len(word)
        dp=[False]*len(sequence)
        for i in range(len(sequence)):
            if sequence[i:i+n]==word:
                dp[i]=True
        ans=0
        for i in range(len(sequence)):
            temp=0
            j=i
            while j<len(sequence) and dp[j]==True:
                temp+=1
                j+=n
            ans=max(ans,temp)
        return ans

        print(dp)
        return 2
            