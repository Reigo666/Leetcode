class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], num: int) -> int:
        x=num
        numl=[]
        ans=0
        n=len(digits)
        for i in range(n):
            digits[i]=int(digits[i])
        mult=len(digits)
        while(x):
            temp=x%10
            numl.append(temp)
            x=x//10
            ans+=mult
            mult*=n
            #print(ans)
        numl=numl[::-1]
        print(numl,ans)
        def check(idx):
            #n=len(digits)
            for i in range(n):
                if digits[i]>numl[idx]:
                    nonlocal ans
                    ans-=n**(len(numl)-idx-1)
                elif digits[i]<numl[idx]:
                    continue
                else:
                    if idx<len(numl)-1:
                        check(idx+1)
        check(0)
        return ans


        
       


        
