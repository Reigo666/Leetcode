class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        vec=[]
        K=2
        for i in range(len(nums)):
            vec.append([nums[i],i])
        
        vec.sort(key=lambda x:(-x[0],x[1]))
        #print(vec)
        
        sl=[]
        ans=[0]*len(nums)

        for i in range(len(vec)):
            val,pos=vec[i]
            idx=bisect.bisect(sl,pos)

            if idx+K-1<len(sl):
                ans[pos]=nums[sl[idx+K-1]]
            else:
                ans[pos]=-1
            sl.insert(idx,pos)
        return ans
