class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ansprob=set()
        seen=set()

        for num in nums:
            if num in seen:
                if num in ansprob:
                    ansprob.remove(num)
            else:
                seen.add(num)
                ansprob.add(num)
            
        
        for num in ansprob:
            return num
        return -1