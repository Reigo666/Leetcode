class Trie:
    def __init__(self,words):
        self.d={}
        for word in words:
            d=self.d
            for l in word:
                if l not in d:
                    d[l]={}
                d=d[l]
            d['end']=word
    
    def serach(self,word):
        
        d=self.d
        matches=[]
        for l in word:
            if l not in d:
                break
            d=d[l]
            if 'end' in d:
                matches.append(d['end'])
        return matches

class Solution:
    def multiSearch(self, big: str, smalls: List[str]) -> List[List[int]]:
        t=Trie(smalls)
        dict=defaultdict(list)


        for i in range(len(big)):
            matches=t.serach(big[i:])
            #print(matches)
            for match in matches:
                dict[match].append(i)
        
        ans=[]
        for word in smalls:
            ans.append(dict[word])
        return ans



