
from typing import List,Optional

class Solution:
    #原想法 push一个进去然后插空
    #新想法 从先到后排列
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        lens=len(nums)
        used=[0]*lens
        def backTrack(combination:List,nums,used:List):
            if 0 not in used:
                ans.append(combination)
                return
            else:
                lastnum=nums[0]-1
                for i in range(lens):
                    if used[i]==1:
                        continue
                    else:
                        if lastnum==nums[i]:
                            continue                       
                        used[i]=1
                        backTrack(combination+[nums[i]],nums,used)
                        used[i]=0
                        lastnum=nums[i]

                 
        backTrack([],nums,used)
        
        
        return ans


sol=Solution()
nums1 = [1,1,2]
nums2 = [2,2,1,1]
print(sol.permuteUnique(nums2))

# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]

# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

