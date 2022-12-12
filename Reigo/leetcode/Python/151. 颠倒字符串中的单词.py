class Solution:
    def reverseWords(self, s: str) -> str:
        n=len(s)
        i=0
        wordlist=[]
        while i<=n-1:
            while i<=n-1 and s[i]==" ":
                i+=1
            word=""
            while i<=n-1 and s[i]!=" ":
                word+=s[i]
                i+=1
            if word=="":
                break
            wordlist.append(word)
        wordlist=wordlist[::-1]
        return " ".join(wordlist)