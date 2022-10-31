class Solution:
    def magicalString(self, n: int) -> int:
        if n<=3:
            return 1
        
        s="122"
        l=2

        numof1=1
        turn='1'
        while len(s)<n:
            if s[l]=='1':
                add=1
            else:
                add=2

            if turn=='1':
                numof1+=add
                s+='1'*add
                turn='2'
            else:
                s+='2'*add
                turn='1'
            l+=1
        if len(s)>n:
            if s[-1]=='1':
                numof1-=1
        return numof1
