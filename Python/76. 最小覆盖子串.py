
import collections
from typing import  List,Optional
import copy


class Solution:
    #检查sdict是否满足条件
    def isValid(self,sdict:dict,tdict:dict)->bool:
        for key in tdict.keys():
            if sdict[key]<tdict[key]:
                return False
        return True
    def minWindow(self, s: str, t: str) -> str:
        tdict={}
        for letter in t:
            if letter not in tdict.keys():
                tdict[letter]=1
            else:
                tdict[letter]+=1
        print(tdict)

        sdict={}
        for key in tdict.keys():
            sdict[key]=0
        
        l=0
        r=0
        bestl=-1
        bestr=-1
        bestdis=2**31-1
        isvalid=0
        templetter=''
        while r<=len(s)-1:
            templetter=s[r]
            if s[r] in tdict.keys():
                sdict[s[r]]+=1
                if self.isValid(sdict,tdict):
                    if r-l+1<bestdis:
                        bestdis=r-l+1
                        bestl=l
                        bestr=r
                        isvalid=1
                    #找最优解
                    while True:
                        #把s[l]删掉后是否满足？
                        if s[l] in tdict.keys():
                            sdict[s[l]]-=1
                            #可以删除
                            if self.isValid(sdict,tdict):
                                if r-l<bestdis:
                                    bestl=l+1
                                    bestr=r
                                    bestdis=r-l
                            #不能删除
                            else:
                                sdict[s[l]]+=1
                                break
                        elif s[l] not in tdict.keys():
                            if r-l<bestdis:
                                bestl=l+1
                                bestr=r
                                bestdis=r-l
                        l+=1
            r+=1
        return s[bestl:bestr+1]


    def minWindow1(self, s: str, t: str) -> str:
        need=collections.defaultdict(int)
        for c in t:
            need[c]+=1
        needCnt=len(t)
        i=0
        res=(0,float('inf'))
        for j,c in enumerate(s):
            if need[c]>0:
                needCnt-=1
            need[c]-=1
            if needCnt==0:       #步骤一：滑动窗口包含了所有T元素
                while True:      #步骤二：增加i，排除多余元素
                    c=s[i] 
                    if need[c]==0:
                        break
                    need[c]+=1
                    i+=1
                if j-i<res[1]-res[0]:   #记录结果
                    res=(i,j)
                need[s[i]]+=1  #步骤三：i增加一个位置，寻找新的满足条件滑动窗口
                needCnt+=1
                i+=1
        return '' if res[1]>len(s) else s[res[0]:res[1]+1]    #如果res始终没被更新过，代表无满足条件的结果

sol=Solution()
s = "ADOBECODEBANCEEE"
t = "ABC"
print(sol.minWindow1(s,t))

# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"