class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        """ 
            第i个数,替换了j次
            dp[i][j]=arr1[i] #假设这次不用替换 arr1[i]>dp[i-1][j]
                    =min(arr2>dp[i-1][j-1] )    #假设这次需要替换arr2
        """
        #1 10000 3 4 5
        #2
        arr2.sort()
        #arr2去重
        for i in range(len(arr2)-1,0,-1):
            if arr2[i]==arr2[i-1]:
                arr2.pop(i)
        n=len(arr1)
        dp=[[inf]*(n+1) for _ in range(n)]
        dp[0][0]=arr1[0]
        dp[0][1]=arr2[0]
        # r=0
        ans=-1
        for i in range(1,n):
            for j in range(i+2):
                if arr1[i]>dp[i-1][j]:
                    dp[i][j]=arr1[i]
                idx=bisect.bisect_right(arr2,dp[i-1][j-1])
                if idx<len(arr2):
                    dp[i][j]=min(dp[i][j],arr2[idx])
        
        #print(dp)
        for j in range(n+1):
            if dp[n-1][j]!=inf:
                return j

        if ans==-1:
            return -1
        return ans
                
                

