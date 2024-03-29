class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dict=defaultdict(int)
        a=25
        for l in order:
            dict[l]-=a
            a-=1
        
        def check(s1,s2):
            if len(s1)==0:
                return True
            else:
                if len(s2)==0:
                    return False
                if s1[0]==s2[0]:
                    if check(s1[1:],s2[1:]):
                        return True
                    return False
                else:
                    if dict[s1[0]]<dict[s2[0]]:
                        return True
                    else:
                        return False
            return False
        
        for i in range(1,len(words)):
            if not check(words[i-1],words[i]):
                return False
        return True
    
    def isAlienSorted1(self, words: List[str], order: str) -> bool:
        dict={}
        tmp=0

        for l in order:
            dict[l]=chr(ord('a')+tmp)
            tmp+=1

        pre=''
        for i in range(len(words)):
            newword=''
            for j in range(len(words[i])):
                newword+=dict[words[i][j]]
            words[i]=newword
            if words[i]<pre:
                return False
            pre=words[i]
        return True
