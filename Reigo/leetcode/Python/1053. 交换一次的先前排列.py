class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        #[2,3,4,1,7,3,7,1,9]
        #[1,2,3,7,5,6,4,8,9]
        #[8,7,8]
        #找比自己小的但最大的 改后面会最大 即从后往前找第一个升序对

        #仍是单调栈原理 找到第一个升序对时 这个值一定是要交换的
        n=len(arr)
        for i in range(n-1,0,-1):
            #找到了升序对
            if arr[i-1]>arr[i]:
                idx=i
                for j in range(i+1,n):
                    #已经找到答案
                    if arr[j]>=arr[i-1]:
                        break
                    else:
                        if arr[j]!=arr[idx]:
                            idx=j
                #print(i-1,idx)
                arr[i-1],arr[idx]=arr[idx],arr[i-1]
                break
        return arr



        # s=[]
        # i=len(arr)-1
        # while i>=0:
        #     temp=-1
        #     while s and arr[i]>=arr[s[-1]]:
        #         idx=s.pop()
        #         if arr[i]>arr[idx]:
        #             temp=t
        #     if temp!=-1:
        #         arr[i],arr[temp]=arr[temp],arr[i]
        #         return arr
        #     s.append(i)
        #     i-=1
        # return arr
        
            