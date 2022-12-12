class Solution:
    def minOperations(self, s: str) -> int:
        cnt1=0
        cnt2=0
        rev=True
        for l in s:
            if rev:
                if l=='0':
                    cnt2+=1
                elif l=='1':
                    cnt1+=1
            
            else:
                if l=='1':
                    cnt2+=1
                elif l=='0':
                    cnt1+=1
            rev=not rev
        
        return min(cnt1,cnt2)
