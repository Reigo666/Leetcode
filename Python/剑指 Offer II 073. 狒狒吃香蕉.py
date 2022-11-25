class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def retNeedHour(piles,k):
            ret=0
            if k==0:
                return inf
            for i in range(len(piles)):
                ret+=(piles[i]+k-1)//k
            
            return ret
        #吃的速度
        l=sum(piles)//h
        r=max(piles)

        while l<r:
            mid=(l+r)//2
            needhour=retNeedHour(piles,mid)
            if needhour>h:
                l=mid+1
            elif needhour<=h:
                r=mid
        
        return l