
import collections
from typing import  List,Optional

class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp=collections.defaultdict(list)

        for str in strs:
            keystr="".join(sorted(str))
            mp[keystr].append(str)
        #print(mp.values())
        return list(mp.values())


        
sol=Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(sol.groupAnagrams(strs))



# 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出: [["bat"],["nat","tan"],["ate","eat","tea"]]



