class Solution:
    def longestDecomposition(self, text: str) -> int:
        #gaigi  gigai

        def dfs(str):
            #print()
            #print(str)
            if len(str)==0:
                return 0
            l=0
            r=len(str)-1
            lch=str[0]
            rch=str[r]

            for i in range(r):
                if str[i]==rch:
                    if lch==str[r-i]:
                        if str[:i+1]==str[-i-1:]:
                            #print(str[:i+1],str[-i-1:])
                            return dfs(str[i+1:-i-1])+2
            return 1
        
        return dfs(text)