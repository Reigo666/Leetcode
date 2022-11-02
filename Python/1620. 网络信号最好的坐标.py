class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        def solveAns(point):
            res=0
            for tower in towers:
                pointa,powera=tower[0:2],tower[2]
                dis=calcDis(pointa,point)
                #print(pointa,point,dis,radius)
                if dis<=radius:
                    res+=floor(powera/(1+dis))
            #print(point,res)
            return res

        def calcDis(pointa,pointb):
            dx,dy=pointa
            tx,ty=pointb
            return ((tx-dx)**2+(ty-dy)**2)**(0.5)
        
        ma=-1
        maxpoint=[-1,-1]
        for i in range(51):
            for j in range(51):
                p=solveAns([i,j])
                if p>ma:
                    maxpoint=[i,j]
                    ma=p
                elif p==ma:
                    temp=[maxpoint,[i,j]]
                    temp.sort()
                    maxpoint=temp[0]
                #print(i,j,maxpoint,ma)
        return maxpoint