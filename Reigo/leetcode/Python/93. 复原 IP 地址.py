
import collections
from typing import  List,Optional
import copy

from matplotlib.style import available

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s)<=3:
            return []
        ans=[]
        #combination list 最终为四个数字
        def isAvail(s):
            if len(s)==1:
                return True
            else:
                if s[0]=='0':
                    return False
                if int(s)>=0 and int(s)<=255:
                    return True
            return False
        def backTrack(combination:List[str],s,k,ansnum):
            if not s:
                if ansnum==4:
                    ans.append(".".join(combination))
                else:
                    return
            else:
                combination.append(s[0])
                if k-1<=(3-ansnum)*3:
                    backTrack(combination,s[1:],k-1,ansnum+1)
                combination.pop()
                if k>=2 and k-2<=(3-ansnum)*3:
                    combination.append(s[0:2])
                    if isAvail(combination[-1]):
                        backTrack(combination,s[2:],k-2,ansnum+1)
                    combination.pop()
                if k>=3 and k-3<=(3-ansnum)*3:
                    combination.append(s[0:3])
                    if isAvail(combination[-1]):
                        backTrack(combination,s[3:],k-3,ansnum+1)
                    combination.pop()
                
        backTrack([],s,len(s),0)
        return ans
sol=Solution()
s = "25525511135"
print(sol.restoreIpAddresses(s))

# 输入：s = "25525511135"
# 输出：["255.255.11.135","255.255.111.35"]


