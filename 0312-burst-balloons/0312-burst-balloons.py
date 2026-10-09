class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = [1]+nums+[1]
        n = len(a)
        dp = [[0]*(n) for _ in range(n)]
        for l in range(2,n):
            for i in range(0,n-l):
                j = i+l
                for k in range(i+1,j):
                   dp[i][j]= max(dp[i][j],dp[i][k] + dp[k][j] + a[i] * a[k] * a[j])
        return dp[0][n - 1]