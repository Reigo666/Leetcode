class Solution:
    def isRobotBounded(self, instructions: str) -> bool:

        def calc(curdir,dx,dy,ch):
            if ch=='G':
                if curdir==0:
                    dy+=1
                elif curdir==90:
                    dx+=1
                elif curdir==180:
                    dy-=1
                elif curdir==270:
                    dx-=1
            elif ch=='L':
                curdir-=90
                if curdir<0:
                    curdir+=360
            elif ch=='R':
                curdir+=90
                if curdir>=360:
                    curdir-=360
            return curdir,dx,dy
            


        dir1=0
        x,y=0,0
        for i in range(4):
            for ch in instructions:
                dir1,x,y=calc(dir1,x,y,ch)
            if x==0 and y==0:
                return True
        return False