class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red=defaultdict(list)
        blue=defaultdict(list)

        for e in redEdges:
            s,t=e
            red[s].append(t)

        for e in blueEdges:
            s,t=e
            blue[s].append(t)

        visit=[[False]*2 for _ in range(n)]
        dp=[[-1]*2 for _ in range(n)]
        q=deque([(0,0),(0,1)])

        length=0
        while q:
            for i in range(len(q)):
                s,color=q.popleft()
                if visit[s][color]:
                    continue
                visit[s][color]=True
                if dp[s][color]==-1:
                    dp[s][color]=length
                else:
                    dp[s][color]=min(dp[s][color],length)
                
                if color==0:
                    dict1=blue
                else:
                    dict1=red
                for t in dict1[s]:
                    q.append((t,1-color))
            length+=1
        ans=[]
        for i in range(n):
            a,b=dp[i]
            if a!=-1 and b!=-1:
                ans.append(min(a,b))
            else:
                ans.append(max(a,b))
        return ans
                