from typing import List,Optional

class Solution:
    def countAndSay(self, n: int) -> str:
        prev='1'
        for i in range(n-1):
            curr=""
            lens=len(prev)
            j=0
            while j<lens:
                start=j
                while j<lens-1 and prev[j+1]==prev[j]:
                    j+=1
                j+=1
                curr+=str(j-start)+prev[start] 
            prev=curr
        return prev
sol=Solution()

n1=5
print(sol.countAndSay(n1))

# 输入：n = 4
# 输出："1211"