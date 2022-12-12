from typing import List,Optional

class Solution:
    #回溯 排序 剪枝
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        candidates.sort()
        def backTrack(combination,target,candidates):
            if target==0:
               ans.append(combination)
            elif target<0:return
            elif target>0:
                lens=len(candidates)
                for i in range(lens):
                    #剪枝
                    if target-candidates[i]<0:break
                    backTrack(combination+[candidates[i]],target-candidates[i],candidates[0:i+1])
        temp=[]
        backTrack(temp,target,candidates)
        return ans
sol=Solution()

candidates1 = [2,3,5]
target1 = 8

candidates2 =[2,3,6,7]
target2 = 7

print(sol.combinationSum(candidates2,target2))

# 输入：candidates = [2,3,6,7], target = 7
# 输出：[[2,2,3],[7]]

# 输入: candidates = [2,3,5], target = 8
# 输出: [[2,2,2,2],[2,3,3],[3,5]]