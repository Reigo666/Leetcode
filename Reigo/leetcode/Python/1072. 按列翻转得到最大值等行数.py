class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        dict1=defaultdict(int)
        for i in range(m):
            temp=0
            for j in range(n):
                temp=temp*2+matrix[i][j]
            dict1[temp]+=1
        
        ans=1
        #print(dict1)
        MAX=2**n-1
        for k,v in dict1.items():
            kk=MAX^k
            #print(kk)
            if kk in dict1:
                cur_ans=v+dict1[kk]
                #print(kk,v,dict1[kk])
                ans=max(ans,cur_ans)
            ans=max(ans,v)
        return ans
        
        #[[1,0,0,0,1,1,1,0,1,1,1],
        # [1,0,0,0,1,0,0,0,1,0,0],
        # [1,0,0,0,1,1,1,0,1,1,1],
        # [1,0,0,0,1,0,0,0,1,0,0],
        # [1,1,1,0,1,1,1,0,1,1,1]]