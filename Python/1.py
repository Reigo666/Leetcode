from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n, ans = len(arr), 0
        j, minv, maxv = 0, n, -1
        for i in range(n):
            minv, maxv = min(minv, arr[i]), max(maxv, arr[i])
            if j == minv and i == maxv:
                ans, j, minv, maxv = ans + 1, i + 1, n, -1
        return ans

sol=Solution()
print(sol.maxChunksToSorted([1,0,2,3,4]))