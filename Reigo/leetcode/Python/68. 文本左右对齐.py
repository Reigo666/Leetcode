
import collections
from typing import  List,Optional
import copy

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        anslist=[]
        templist=[]
        tempnum=0
        for str in words:
            lens=len(str)
            if lens+tempnum>maxWidth:
                #推出最后的空格
                templist.pop()
                tempnum-=1
                #余下的空格
                restspace=maxWidth-tempnum
                #分配剩余的空格
                #共有spacenum个空格位置
                lenn=len(templist)
                spacenum=lenn//2

                #如果只有一个单词
                if spacenum==0:
                    templist.append(" "*restspace)
                #如果有多个单词
                elif spacenum!=0:
                    #每个空位需要加addspc个空格
                    addspc=restspace//spacenum
                    #余下多余的空格数
                    restspc=restspace%spacenum
                    
                    #为所有地方分配空格
                    for j in range(spacenum): 
                        if restspc:
                            templist[j*2+1]+=(addspc+1)*' '
                            restspc-=1
                        else:
                            templist[j*2+1]+=addspc*' '
                #加入答案
                anslist.append("".join(templist))
                #加入这次的到下次
                templist=[str]
                templist.append(' ')
                tempnum=lens+1
            elif lens+tempnum<maxWidth:
                templist.append(str)
                tempnum+=lens
                templist.append(' ')
                tempnum+=1
            elif lens+tempnum==maxWidth:
                templist.append(str)
                anslist.append("".join(templist))
                templist=[]
                tempnum=0
        
        #分配最后一行
        if templist!=[]:
            templist.pop()
            tempnum-=1
            restspace=maxWidth-tempnum
            templist.append(" "*restspace)
            anslist.append("".join(templist))
        return anslist
sol=Solution()
words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
print(sol.fullJustify(words,maxWidth))
# 输入:words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]，maxWidth = 20
# 输出:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]

