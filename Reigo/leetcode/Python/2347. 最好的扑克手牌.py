class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        color=None
        isFlush=True
        for s in suits:
            if color==None:
                color=s
            else:
                if color!=s:
                    isFlush=False
                    break

        if isFlush:
            return 'Flush'
        
        cnt=Counter(ranks)
        isPair=False
        for k in cnt:
            if cnt[k]>=3:
                return "Three of a Kind"
            elif cnt[k]==2:
                isPair=True
        if isPair:
            return "Pair"
        return "High Card"
        