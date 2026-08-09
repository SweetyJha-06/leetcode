class Solution:
    def stoneGameII(self, piles):
        n = len(piles)
        suf = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suf[i] = suf[i + 1] + piles[i]

        dp = {}

        def f(i, m):
            if i >= n:
                return 0
            if (i, m) in dp:
                return dp[i, m]

            best = 0
            for x in range(1, 2 * m + 1):
                if i + x > n:
                    break
                best = max(best, suf[i] - f(i + x, max(m, x)))

            dp[i, m] = best
            return best

        return f(0, 1)