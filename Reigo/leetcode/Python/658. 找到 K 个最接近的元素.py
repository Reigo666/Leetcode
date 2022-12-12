class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        idx=bisect.bisect(arr,x)
        if idx==len(arr):
            return arr[idx-k:idx]
        elif idx==0:
            return arr[0:k]
        
        l=idx-1
        r=idx

        while k and l>=0 and r<len(arr):
            if abs(arr[l]-x)<=abs(arr[r]-x):
                l-=1
            else:
                r+=1
            k-=1
        if k and l>=0:
            l-=k
        else:
            r+=k
        
        print(l,r)
       
        return arr[l+1:r]
        


        