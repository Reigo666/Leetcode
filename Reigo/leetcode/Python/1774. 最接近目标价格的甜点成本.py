class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        ans=baseCosts[0]
        def dfs(left,cur):
            nonlocal ans
            #print(cur)
            if abs(cur-target)>abs(ans-target):
                if cur>ans:
                    return

            if abs(cur-target)<=abs(ans-target):
                if abs(cur-target)==abs(ans-target):
                    if cur<ans:
                        ans=cur
                else:
                    ans=cur

            if not left:
                return
            
            for i in range(3):
                dfs(left[1:],cur+left[0]*i)
        
        for base in baseCosts:
            dfs(toppingCosts,base)
        return ans
