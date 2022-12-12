class Solution:
    def squareIsWhite(self, c: str) -> bool:
        #odd is White
        a=c[0]
        b=c[1]

        a=ord(a)-ord('a')+1
        if (a+int(b))%2:
            return True
        return False