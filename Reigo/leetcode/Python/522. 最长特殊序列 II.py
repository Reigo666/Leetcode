import collections
from typing import  List,Optional
import copy
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        strs=sorted(strs,key=lambda x:len(x),reverse=True)
        n=len(strs[0])
        i=0
        prelist=[]
        def checkSubStr(str,l):
            n=len(str)
            for s in l:
                k=0
                j=0
                while j<len(s):
                    if str[k]==s[j]:
                        k+=1
                        j+=1
                    else:
                        j+=1
                    if k==len(str):
                        return True
            return False
        while i<len(strs):
            dict=collections.defaultdict(int)
            n=len(strs[i])
            while i<len(strs) and len(strs[i])==n:
                dict[strs[i]]+=1
                i+=1
            for k in dict:
                if dict[k]==1:
                    if not checkSubStr(k,prelist):
                        return n
            for k in dict:
                prelist.append(k)
        return -1