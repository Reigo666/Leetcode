class Solution:
    def maxProduct(self, words: List[str]) -> int:
        masks=[0]*len(words)

        for i,word in enumerate(words):
            for l in word:
                masks[i]|=1<<(ord(l)-ord('a'))
        ans=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if masks[i]&masks[j]==0:
                    ans=max(ans,len(words[i])*len(words[j]))
        return ans


