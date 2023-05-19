class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        pre=0
        maxtime=0
        maxidx=-1
        for log in logs:
            id1,leave=log
            if leave-pre>maxtime:
                maxidx=id1
                maxtime=leave-pre
            elif leave-pre==maxtime:
                maxidx=min(id1,maxidx)
            pre=leave
        return maxidx