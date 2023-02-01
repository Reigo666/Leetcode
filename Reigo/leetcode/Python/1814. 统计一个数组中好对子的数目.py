class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        dict=defaultdict(int)
        __MOD__=10**9 + 7
        def solve(x):
            rev=str(x)
            rev=int(rev[::-1])
            #print(x,rev,x-rev)
            return x-rev
        
        for num in nums:
            dict[solve(num)]+=1
        
        ans=0

        def calcnum(x):
            return (x)*(x-1)//2


        print(dict)
        for k in dict:
            ans+=calcnum(dict[k])%__MOD__
        
        return ans%__MOD__
