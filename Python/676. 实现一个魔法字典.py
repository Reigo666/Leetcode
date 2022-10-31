import collections
from typing import  List,Optional
import copy
class MagicDictionary:

    def __init__(self):
        self.dict=collections.defaultdict(list)

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.dict[len(word)].append(word)

    def search(self, searchWord: str) -> bool:
        n=len(searchWord)
        #print(self.dict[n])
        for word in self.dict[n]:
            difl=0
            for i in range(n):
                if searchWord[i]!=word[i]:
                    difl+=1
                if difl>=2:
                    break
            if difl==1:
                return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)