from typing import List



class Solution:
    #递归的使用 (注意python列表的复制不能直接用等号 但是可以用切片和+组合生成临时值)
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        #当前组合为combination，nleft为能剩余生成的(数,lists表示当前的栈
        def backTrack(combination,nleft,lists):
            if nleft==0 and lists==[]:
                ans.append(combination)
            else:
                if nleft!=0:
                    backTrack(combination+'(',nleft-1,lists+['('])
                #如果有(可以弹出左(
                if lists!=[]:
                    #有左括号
                    if lists[-1]=='(':
                        backTrack(combination+')',nleft,lists[0:-1])
        backTrack("",n,[])
        return ans
    
sol=Solution()
n1 = 3
print(sol.generateParenthesis(n1))



# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]