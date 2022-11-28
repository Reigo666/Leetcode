class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def backTrack(combination,left):
            if not left:
                ans.append(combination)
            else:
                backTrack(combination+[left[0]],left[1:])
                backTrack(combination,left[1:])
        backTrack([],nums)
        return ans