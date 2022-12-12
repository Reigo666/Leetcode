import collections
from typing import  List,Optional
import copy
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        list1=[]
        list2=[]
        for i in range(len(logs)):
            logs[i]=logs[i].split(" ")
            if logs[i][1].isdigit():
                list2.append(logs[i])
                list2[-1]=[list2[-1][0]]+[" ".join(list2[-1][1:])]
            else:
                list1.append(logs[i])
                list1[-1]=[list1[-1][0]]+[" ".join(list1[-1][1:])]
        list1=sorted(list1,key=lambda x:(x[1],x[0]))
        print(list1)
        print(list2)
        list1=list1+list2
        for i in range(len(list1)):
            list1[i]=" ".join(list1[i])
        return list1
            

sol=Solution()
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(sol.reorderLogFiles(logs))

# 输入：logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# 输出：["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
# 解释：
# 字母日志的内容都不同，所以顺序为 "art can", "art zero", "own kit dig" 。
# 数字日志保留原来的相对顺序 "dig1 8 1 5 1", "dig2 3 6" 。

