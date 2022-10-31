
import collections
from multiprocessing import dummy
from typing import  List,Optional
import copy

class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans=[0,1]
        for i in range(2,n+1):
            ans=ans+[num+2**(i-1) for num in ans[::-1]]
            #print(ans)
        return ans
    def grayCode1(self, n: int) -> List[int]:
        ans=[0,1]
        for i in range(2,n+1):
            for j in range(2**i//2,2**i):
                ans.append(ans[2**i-1-j]+2**(i-1))
        return ans

sol=Solution()
n=4
print(sol.grayCode(n))




# 输入：n = 2
# 输出：[0,1,3,2]
# 解释：
# [0,1,3,2] 的二进制表示是 [00,01,11,10] 。
# - 00 和 01 有一位不同
# - 01 和 11 有一位不同
# - 11 和 10 有一位不同
# - 10 和 00 有一位不同
# [0,2,3,1] 也是一个有效的格雷码序列，其二进制表示是 [00,10,11,01] 。
# - 00 和 10 有一位不同
# - 10 和 11 有一位不同
# - 11 和 01 有一位不同
# - 01 和 00 有一位不同



