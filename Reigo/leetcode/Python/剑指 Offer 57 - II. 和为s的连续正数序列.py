class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        l=1
        r=1

        sum1=0
        ans=[]
        while r<=(target+1)//2+1:
            sum1+=r
            while sum1>target:
                sum1-=l
                l+=1
            if sum1==target:
                if r-l+1>=2:
                    ans.append(list(range(l,r+1)))
            
            r+=1
        return ans
            
