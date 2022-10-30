class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        #nums.sort()
        dict=defaultdict(list)
        
        for num in nums:
            x=num%space
            bisect.insort(dict[x],num)
        
        ansmax=0
        ans=None
        for k in dict:
            if len(dict[k])>ansmax:
                ans=dict[k][0]
                ansmax=len(dict[k])
            elif len(dict[k])==ansmax:
                ans=min(ans,dict[k][0])
                
        #print(dict)
        return ans