class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m=len(rowSum)
        n=len(colSum)
        ans=[]
        for i in range(m):
            temp=[]
            for j in range(n):
                cur=min(rowSum[i],colSum[j])
                rowSum[i]-=cur
                colSum[j]-=cur
                temp.append(cur)
            ans.append(temp)
        
        return ans