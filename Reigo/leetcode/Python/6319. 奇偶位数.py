class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even=0
        odd=0
        evenTurn=True
        for i in range(32):
            if n>>i&1:
                if evenTurn:
                    even+=1
                else:
                    odd+=1
            evenTurn=not evenTurn
        return [even,odd]