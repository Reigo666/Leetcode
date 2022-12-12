class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l1=version1.split(".")
        l2=version2.split(".")
        len1=len(l1)
        len2=len(l2)
        if len1<len2:
            l1+=['0']*(len2-len1)
        elif len2<len1:
            l2+=['0']*(len1-len2)
        for i in range(max(len1,len2)):           
            if int(l1[i])<int(l2[i]):
                return -1
            elif int(l1[i])>int(l2[i]):
                return 1
            else:
                continue
        return 0