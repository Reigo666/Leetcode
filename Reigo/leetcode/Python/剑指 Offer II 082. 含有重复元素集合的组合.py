class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        candidates.sort()
        def backTrack(combination,candidates,target):
            if target<0:
                return
            elif target==0:
                ans.append(combination)
            elif len(candidates)==0:
                return
            else:
                pre=candidates[0]
                l=0
                while l<len(candidates) and candidates[l]==pre:
                    l+=1
                
                for i in range(l+1):
                    backTrack(combination+[pre]*i,candidates[l:],target-pre*i)

                    
                #backTrack(combination,candidates[1:],target)
                #backTrack(combination+[candidates[0]],candidates[1:],target-candidates[0])
        
        backTrack([],candidates,target)
        return ans

