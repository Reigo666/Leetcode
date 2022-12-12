class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        dict=defaultdict(list)
        for i in range(len(s)):
            dict[s[i]].append(i)
        #print(dict)
        ans=0
        for word in words:
            l=-1
            isValid=True
            for let in word:
                if let in dict:
                    idx=bisect.bisect_left(dict[let],l+1)
                    #print(idx)
                    if idx==len(dict[let]):
                        isValid=False
                        break
                    l=dict[let][idx]
                else:
                    isValid=False
                    break
                #print(l)
            if isValid:
                ans+=1
        return ans