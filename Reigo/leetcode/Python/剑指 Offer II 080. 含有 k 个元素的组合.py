class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        def backTrack(combination,temp,limit,k):
            if k==0:
                ans.append(combination)
            elif temp>limit:
                return
            else:
                backTrack(combination+[temp],temp+1,limit,k-1)
                backTrack(combination,temp+1,limit,k)
        backTrack([],1,n,k)
        return ans
    
