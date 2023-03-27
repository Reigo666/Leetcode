class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        m=len(s)
        n=len(t)
        ans=0
        for i in range(m):
            for j in range(n):
                #以i，j开头
                ii=i
                jj=j
                diff=0
                while ii<m and jj<n:
                    #print(ans,ii,jj,diff)
                    if s[ii]!=t[jj]:
                        diff+=1
                        if diff>=2:
                            break
                    if diff==1:
                        ans+=1
                        # print(ans,i,j)
                        # print(ii,jj)
                    ii+=1
                    jj+=1
        return ans
                    