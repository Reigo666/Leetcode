import collections
from typing import  List,Optional
import copy

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        dict={}
        setl=set()
        ans=[]
        for i in range(len(words)):
            if len(words[i])==len(pattern):
                valid=True
                for j in range(len(pattern)):
                    if words[i][j] not in dict:
                        dict[words[i][j]]=pattern[j]
                        if pattern[j] in setl:
                            valid=False
                            break
                        else:
                            setl.add(pattern[j])
                    else:
                        if dict[words[i][j]]!=pattern[j]:
                            valid=False
                            break
                if valid:
                    ans.append(words[i])
                dict={}
                setl.clear()
        return ans

sol=Solution()
words=["mee"]
pattern="abb"
print(sol.findAndReplacePattern(words,pattern))