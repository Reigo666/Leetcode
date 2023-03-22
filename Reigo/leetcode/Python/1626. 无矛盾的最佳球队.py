class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        #ages 1,8,9,10,11,12,13,14
        #scor 5,1,2, 3, 7, 3, 3, 3 3 3 3
        sa=list(zip(scores,ages))
        sa.sort(key=lambda x:(x[1],x[0]))

        #print(sa)
        ans=0
        dp=[0]*len(scores)
        for i in range(len(ages)):
            curscore,curage=sa[i]
            dp[i]=curscore
            for j in range(i):
                # #年龄相等可直接加
                # if sa[j][1]==curage:
                #     dp[i]=max(dp[i],curscore+dp[j])
                # else:
                #年龄不等需要分数有差距
                if sa[j][0]<=curscore:
                    dp[i]=max(dp[i],curscore+dp[j])
            ans=max(ans,dp[i])
            #print(dp)
        return ans
                