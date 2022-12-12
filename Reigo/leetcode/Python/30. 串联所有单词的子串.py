from typing import List,Optional

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        lenwords=len(words)
        dicwords={}
        for i in range (lenwords):
            val=dicwords.get(words[i],0)
            dicwords[words[i]]=val+1
        print(dicwords)

        lens=len(s)
        lenwordsword=len(words[0])
        ans=[]
        for i in range(lens-lenwords*lenwordsword+1):
            num=0
            dic={}
            for j in range(lenwords):
                
                tempword=s[i+j*lenwordsword:i+j*lenwordsword+lenwordsword]
                if tempword not in dicwords.keys():
                    break
                else:
                    val=dic.get(tempword,0)
                    dic[tempword]=val+1
                    if val+1>dicwords[tempword]:
                        break
                    num+=1
            if num==lenwords:
                ans.append(i)
        return ans