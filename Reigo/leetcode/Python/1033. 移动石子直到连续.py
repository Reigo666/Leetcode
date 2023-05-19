class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        arr=[a,b,c]
        arr.sort()

        a,b,c=arr

        if b-a==1 and c-b==1:
            return [0,0]

        minv=2
        if b-a==1 or b-a==2 or c-b==1 or c-b==2:
            minv=1
        
        return [minv,c-a-2]