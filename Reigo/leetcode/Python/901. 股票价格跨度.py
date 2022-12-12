class StockSpanner:

    def __init__(self):
        self.arr=[]
        self.dp=[]

    def next(self, price: int) -> int:
        arr=self.arr
        dp=self.dp
        if not arr:
            arr.append(price)
            dp.append(0)
            return 1
        else:
            idx=len(arr)
            if price<arr[-1]:
                dp.append(idx)
            else:
                arridx=-1
                cur=arr[arridx]
                while price>=cur:

                    arridx=dp[arridx]-1
                    if arridx==-1:
                        break
                    cur=arr[arridx]
                dp.append(arridx+1)
            arr.append(price)
            return idx-dp[-1]+1


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)