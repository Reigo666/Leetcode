class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def backTrack(combination,left):
            if len(left)==0:
                ans.append(combination)
            else:
                for i in range(len(left)):
                    backTrack(combination+[left[i]],left[:i]+left[i+1:])
        backTrack([],nums)
        return ans
