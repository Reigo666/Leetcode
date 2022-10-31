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
                    #考虑数字重复问题
                    if i<lens-1 and candidates[i]==candidates[i+1]:
                        continue
                    backTrack(combination+[candidates[i]],target-candidates[i],candidates[0:i])
        temp=[]
        backTrack(temp,target,candidates)
        return ans
sol=Solution()

candidates1 = [10,1,2,7,6,1,5]
#candidates1 = [1,1,2,5,6,7,10]
target1 = 8

print(sol.combinationSum(candidates1,target1))

# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 输出:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
