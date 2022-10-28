class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        __MOD__=10**9+7
        stack=[]
        left=[]
        for i in range(len(arr)):
            while stack and arr[i]<=arr[stack[-1]]:
                stack.pop()
            
            if not stack:
                left.append(-1)
            else:
                left.append(stack[-1])
            stack.append(i)
        
        stack.clear()
        right=[0]*len(arr)
        for i in range(len(arr)-1,-1,-1):
            while stack and arr[i]<arr[stack[-1]]:
                stack.pop()
            
            if not stack:
                right[i]=(len(arr))
            else:
                right[i]=(stack[-1])
            stack.append(i)
        #print(left)
        #print(right)
        ans=0
        for i in range(len(arr)):
            ans=(ans+(i-left[i])*(right[i]-i)*arr[i])%__MOD__
        return ans