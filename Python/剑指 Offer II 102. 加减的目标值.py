class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #pos neg
        #pos+neg=total
        #pos-neg=target
        
        total=sum(nums)
        if abs(target)>total:
            return 0
        if (total+target)%2==1:
            return 0
        elif (total-target)%2==1:
            return 0
        pos=(total+target)//2
        neg=(total-target)//2

        cap=min(pos,neg)
        


        dp=[0]*(cap+1)
        dp[0]=1
        for num in nums:
            for j in range(cap,num-1,-1):
                dp[j]+=dp[j-num]
        
        return dp[cap]