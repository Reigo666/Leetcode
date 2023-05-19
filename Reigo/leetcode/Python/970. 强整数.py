class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        a=1

        ans=set()
        while a<bound:
            b=1
            while a+b<=bound:
                ans.add(a+b)
                b*=y
                if y==1:
                    break
            if x==1:
                break
            a*=x
        
        ans=list(ans)
        return ans