from typing import List,Optional

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def backTrack(combination:List,nums):
            if nums==[]:
                ans.append(combination)
                return
            else:
                lenc=len(combination)
                for i in range(lenc+1):
                    backTrack(combination[0:i]+[(nums[0])]+combination[i:],nums[1:])   
        backTrack([],nums)
        return ans


sol=Solution()
nums1 = [1,2,3]
print(sol.permute(nums1))

# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

