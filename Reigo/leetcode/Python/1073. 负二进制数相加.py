class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        #16 -8 4 -2 1
        #1 1
        #0 1

        #0 0
        ans=[]
        i=len(arr1)-1
        j=len(arr2)-1
        c=0
        while i>=0 or j>=0 or c:
            a=0 if i<0 else arr1[i]
            b=0 if j<0 else arr2[j]
            x=a+b+c
            c=0
            if x>=2:
                x-=2
                c=-1
            elif x<0:
                x=1
                c=1
            ans.append(x)
            i-=1
            j-=1
        while len(ans)>1 and ans[-1]==0:
            ans.pop()
        return ans[::-1]