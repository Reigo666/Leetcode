class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s1=''
        for l in s:
            s1+=str(ord(l)-ord('a')+1)

        #print(s1)
        while len(s1)>1 and k:
            sum1=0
            for l in s1:
                sum1+=int(l)
            s1=str(sum1)
            k-=1
        return int(s1)