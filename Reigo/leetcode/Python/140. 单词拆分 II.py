
import collections
from typing import  List,Optional
import copy

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dict=collections.defaultdict(list)
        n=len(wordDict)
        for i in range(n):
            dict[wordDict[i][0]].append(wordDict[i])
        dp=[True]*((len(s))+1)
        ans=[]
        def backTrack(combination:List[str],lefts,n)->bool:
            if not lefts:
                ans.append(" ".join(combination))
            else:
                c=lefts[0]
                if dp[n]==False:
                    return
                ansnumpre=len(ans)
                for word in dict[c]:
                    lenword=len(word)
                    if lefts[:lenword]==word:
                        combination.append(word)
                        
                        backTrack(combination,lefts[lenword:],n-lenword)
                        combination.pop()
                ansnumaft=len(ans)
                if ansnumpre==ansnumaft:
                    dp[n]=False
                    
        backTrack([],s,len(s))
        return ans
sol=Solution()
s = "applepenapple"
wordDict = ["apple", "pen"]

s1 = "catsandog"
wordDict1 = ["cats", "dog", "sand", "and", "cat"]

s2 = "catsanddog" 
wordDict2 = ["cat","cats","and","sand","dog"]
print(sol.wordBreak(s2,wordDict))

# 输入:s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
# 输出:["cats and dog","cat sand dog"]

