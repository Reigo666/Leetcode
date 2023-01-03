class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s=s.split(' ')
        pre=-1
        for num in s:
            if num.isdigit():
                if int(num)<=pre:
                    return False
                pre=int(num)
        return True