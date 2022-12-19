class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        sum1=sum(nums)
        diff=abs(sum1-goal)
        ans=(diff-1+limit)//limit
        return ans