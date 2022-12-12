class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s==t:
            return False
        if len(s)!=len(t):
            return False
        dict=defaultdict(int)
        for l in s:
            dict[l]+=1
        
        for l in t:
            if l not in dict:
                return False
            else:
                dict[l]-=1
                if dict[l]<0:
                    return False
        return True