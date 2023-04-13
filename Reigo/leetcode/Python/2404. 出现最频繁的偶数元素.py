class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        dict=defaultdict(int)
        ans=-1
        maxtime=0
        for num in nums:
            if num%2==0:
                dict[num]+=1
                if dict[num]>maxtime:
                    maxtime=dict[num]
                    ans=num
                elif dict[num]==maxtime:
                    if num<ans:
                        ans=num
        return ans