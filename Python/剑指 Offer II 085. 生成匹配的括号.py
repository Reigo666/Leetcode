class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def backTrack(combination,lb,rb):
            if lb==0 and rb==0:
                ans.append(combination)
            else:
                if lb:
                    backTrack(combination+'(',lb-1,rb+1)
                if rb:
                    backTrack(combination+')',lb,rb-1)
        backTrack("",n,0)
        return ans