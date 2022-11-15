class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s=[]
        ans=[0]*len(temperatures)
        for i in range(len(temperatures)-1,-1,-1):
            if not s:
                s.append(i)
            else:
                temp=temperatures[i]
                while s and temperatures[s[-1]]<=temp:
                    s.pop()
                if s:
                    ans[i]=s[-1]-i
                else:
                    ans[i]=0
                s.append(i)
        
        return ans
