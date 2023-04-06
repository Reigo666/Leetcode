class Solution:
    def maskPII(self, s: str) -> str:
        def getDigit(s):
            ret=''
            for l in s:
                if l.isdigit():
                    ret+=l
            return ret
        if '@' in s:
            s=s.split('@')
            pre,aft=s[0],s[1]
            ret=(pre[0]+'*'*5+pre[-1]+'@'+aft).lower()
            return ret
        else:
            s=getDigit(s)
            if len(s)==10:
                return '***-***-'+s[-4:]
            elif len(s)==11:
                return '+*-***-***-'+s[-4:]
            elif len(s)==12:
                return '+**-***-***-'+s[-4:]
            elif len(s)==13:
                return '+***-***-***-'+s[-4:]