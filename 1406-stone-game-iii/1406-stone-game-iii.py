class Solution:
    def stoneGameIII(self, stoneValue):
        n = len(stoneValue)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            s = 0
            dp[i] = -10**9
            for k in range(3):
                if i + k < n:
                    s += stoneValue[i + k]
                    dp[i] = max(dp[i], s - dp[i + k + 1])

        if dp[0] > 0:
            return "Alice"
        if dp[0] < 0:
            return "Bob"
        return "Tie"