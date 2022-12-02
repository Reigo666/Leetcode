class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        def solve(boxes):
            numof1=[0]*len(boxes)
            numof1[0]=int(boxes[0])
            ret=[0]
            for i in range(1,len(boxes)):
                if boxes[i]=='0':
                    numof1[i]=numof1[i-1]
                else:
                    numof1[i]=numof1[i-1]+1
                
                ret.append(ret[i-1]+numof1[i-1])
            
            return ret
        
        ret1=solve(boxes)
        ret2=solve(boxes[::-1])
        ret2=ret2[::-1]
        for i in range(len(ret1)):
            ret1[i]+=ret2[i]
        
        return ret1