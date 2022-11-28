class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans=[]
        def backTrack(combination,candidates,left):
            if left<0:
                return
            elif left==0:
                ans.append(combination)
                return
            else:
                if len(candidates)==0:
                    return
                if candidates[0]>left:
                    return
                for i in range(left//candidates[0]+1):
                    backTrack(combination+[candidates[0]]*i,candidates[1:],left-i*candidates[0])

        backTrack([],candidates,target)
        return ans