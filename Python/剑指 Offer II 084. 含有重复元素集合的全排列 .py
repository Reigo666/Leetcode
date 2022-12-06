class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        def backTrack(combination,left):
            if len(left)==0:
                ans.append(combination)
            else:
                pre=left[0]
                for i in range(len(left)):
                    if i!=0:
                        if left[i]==left[i-1]:
                            continue
                    backTrack(combination+[left[i]],left[:i]+left[i+1:])
        backTrack([],nums)
        return ans

                        
            