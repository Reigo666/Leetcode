class Solution:
    def twoOutOfThree(self, a: List[int], b: List[int], c: List[int]) -> List[int]:
        sa=set(a)
        sb=set(b)
        sc=set(c)
        return list(sa&sb|sa&sc|sb&sc)
