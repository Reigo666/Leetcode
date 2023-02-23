class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        ans=[0]
        for i in range(1,n+1):
            for j in range(len(ans)-1,-1,-1):
                ans.append((1<<(i-1))|ans[j])
        #print(ans)
        for i in range(len(ans)):
            ans[i]=ans[i]^start
        return ans
