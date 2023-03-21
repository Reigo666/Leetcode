class Solution:
    def distMoney(self, money: int, c: int) -> int:
        if money<c:
            return -1
        if money>c*8:
            return c-1
        if money==c*8:
            return money//8
        if money<c*8:
            money-=c
            t=money//7
            mod=money%7
            if mod!=3:
                return t
            else:
                if t==c-1:
                    return t-1
                return t
        