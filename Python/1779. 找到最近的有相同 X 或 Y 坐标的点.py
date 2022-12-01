class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        ansi=-1
        mindis=inf
        for i in range(len(points)):
            tx,ty=points[i]
            if tx==x or ty==y:
                dis=abs(tx-x)+abs(ty-y)
                if dis<mindis:
                    mindis=dis
                    ansi=i
        
        return ansi