class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])

        bx=-1
        by=-1

        px=-1
        py=-1

        ex=-1
        ey=-1
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='S':
                    px=i
                    py=j
                elif grid[i][j]=='B':
                    bx=i
                    by=j
                elif grid[i][j]=='T':
                    ex=i
                    ey=j
        
        def f(x,y):
            return x*n+y

        visit=[[False]*(m*n) for _ in range((m*n))]
        visit[f(px,py)][f(bx,by)]=True
        q=deque([[px,py,bx,by,0]])
        directions=[0,1,0,-1,0]

        def check(i,j):
            if i>=0 and i<m and j>=0 and j<n and grid[i][j]!='#':
                return True
            return False

        while q:
            for i in range(len(q)):
                px,py,bx,by,d=q.popleft()
                #print(px,py,bx,by,d)
                if bx==ex and by==ey:
                    return d

                for a,b in pairwise(directions):
                    ppx=px+a
                    ppy=py+b
                    bbx=bx+a
                    bby=by+b
                    #如果推到箱子了(注意条件不能写在一起)
                    #print(a,b)
                    if ppx==bx and ppy==by:
                        if check(bbx,bby) and not visit[f(ppx,ppy)][f(bbx,bby)]:
                            q.append([ppx,ppy,bbx,bby,d+1])
                            visit[f(ppx,ppy)][f(bbx,bby)]=True
                    #没推到箱子
                    else:
                        if check(ppx,ppy) and not visit[f(ppx,ppy)][f(bx,by)]:
                            q.appendleft([ppx,ppy,bx,by,d])
                            visit[f(ppx,ppy)][f(bx,by)]=True
        return -1
                    
                



        # #检查人是否可以从某一点 到达 某一点
        # def check(startx,starty,targetx,targety):
        #     visit=[[False]*n for _ in range(m)]
        #     all_direct=[[0,-1],[0,1],[-1,0],[1,0]]
        #     def dfs(sx,sy):
        #         if visit[sx][sy]:
        #             return False
        #         visit[sx][sy]=True
        #         if sx==targetx and sy==targety:
        #             return True
        #         for direct in all_direct:
        #             tx,ty=sx+direct[0],sy+direct[1]
        #             if tx>=0 and tx<m and ty>=0 and ty<n and grid[tx][ty]!='#' and grid[tx][ty]!='B':
        #                 if dfs(tx,ty):
        #                     return True
        #         return False

        #     return dfs(startx,starty)