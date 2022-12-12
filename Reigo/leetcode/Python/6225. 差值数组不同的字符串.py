class Solution:
    def oddString(self, words: List[str]) -> str:
        dict=defaultdict(list)
        for word in words:
            temp=[]
            for i in range(1,len(word)):
                temp.append(ord(word[i])-ord(word[i-1]))
            dict[tuple(temp)].append(word)
        for k in dict:
            if len(dict[k])==1:
                return dict[k][0]