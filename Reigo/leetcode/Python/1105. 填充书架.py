class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n=len(books)
        dp=[inf]*n
        
        dp[0]=books[0][1]

        for i in range(1,n):
            #w,h=books[i]
            tempw=0
            temph=0
            for j in range(i,-1,-1):
                tempw+=books[j][0]
                temph=max(temph,books[j][1])
                if tempw<=shelfWidth:
                    if j>=1:
                        dp[i]=min(dp[i],dp[j-1]+temph)
                    else:
                        dp[i]=min(dp[i],temph)
                else:
                    break
        
        return dp[-1]
                
                
