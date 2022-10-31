
import collections
from typing import  List,Optional
import copy

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True
        #dp[j]=dp[i]+word
        for i in range(n):
            for j in range(i+1,n+1):
                if not dp[i]:
                    break
                if dp[i] and (s[i:j] in  wordDict):
                    dp[j]=True
        return dp[-1]
    def wordBreak1(self, s: str, wordDict: List[str]) -> bool:
        dict=collections.defaultdict(list)
        n=len(wordDict)
        for i in range(n):
            dict[wordDict[i][0]].append(wordDict[i])
        dp=[True]*((len(s))+1)

        def backTrack(lefts,n)->bool:
            if not lefts:
                return True
            else:
                c=lefts[0]
                if dp[n]==False:
                    return False
                for word in dict[c]:
                    lenword=len(word)
                    if lefts[:lenword]==word:
                        if backTrack(lefts[lenword:],n-lenword):
                            return True
                dp[n]=False
                return False
        return backTrack(s,len(s))
sol=Solution()
s = "applepenapple"
wordDict = ["apple", "pen"]
s1 = "catsandog"
 
wordDict1 = ["cats", "dog", "sand", "and", "cat"]
print(sol.wordBreak(s1,wordDict1))


# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
#      注意，你可以重复使用字典中的单词。


# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false