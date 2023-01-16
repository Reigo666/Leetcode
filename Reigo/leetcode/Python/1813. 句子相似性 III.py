class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1=sentence1.split(' ')
        s2=sentence2.split(' ')
        if len(s1)<len(s2):
            s1,s2=s2,s1
        l=0
        r=len(s2)-1

        l1=0
        while l<len(s2):
            if s2[l]==s1[l1]:
                l+=1
                l1+=1
            else:
                break
        
        r1=len(s1)-1
        while l<=r:
            if s2[r]==s1[r1]:
                r1-=1
                r-=1
            else:
                break
        if l>r:
            return True
        return False