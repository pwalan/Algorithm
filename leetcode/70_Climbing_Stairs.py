class Solution:
    def climbStairs(self, n: int) -> int:
        res = {}
        res[0] = 1
        res[1] = 2
        for i in range(2,n):
            res[i] = res[i-2] + res[i-1]
        return res[n-1]