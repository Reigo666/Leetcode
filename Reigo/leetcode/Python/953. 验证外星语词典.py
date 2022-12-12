import collections
from typing import  List,Optional
import copy
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dict={}
        for i in range(26):
            dict[order[i]]=i
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j==len(words[i+1]):
                    return False
                if dict[words[i][j]]==dict[words[i+1][j]]:
                    continue
                elif dict[words[i][j]]<dict[words[i+1][j]]:
                    break
                elif dict[words[i][j]]>dict[words[i+1][j]]:
                    return False
        return True

