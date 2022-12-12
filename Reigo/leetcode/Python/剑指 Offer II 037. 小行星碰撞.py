class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s=[]
        ans=[]
        for a in asteroids:
            if a<0:
                if s:
                    isAlive=True
                    while s:
                        if s[-1]==abs(a):
                            s.pop()
                            isAlive=False
                            break
                        elif s[-1]<abs(a):
                            s.pop()
                        elif s[-1]>abs(a):
                            isAlive=False
                            break
                    if isAlive:
                        ans.append(a)
                else:
                    ans.append(a)
            elif a>0:
                s.append(a)
            #print(ans,s)
        ans+=s
        return ans
