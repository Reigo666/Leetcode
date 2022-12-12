class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        dict=defaultdict(int)
        for i in range(len(wall)):
            presum=0
            for j in range(len(wall[i])):
                presum+=wall[i][j]
                if j!=len(wall[i])-1:
                    dict[presum]+=1
        ans=0
        print(dict)
        for k in dict:
            ans=max(ans,dict[k])
        
        return len(wall)-ans