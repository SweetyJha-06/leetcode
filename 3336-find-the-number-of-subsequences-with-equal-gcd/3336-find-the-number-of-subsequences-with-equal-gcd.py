
class Solution:
    def subsequencePairCount(self, nums):
        MOD = 10 ** 9 + 7
        MAX = 200

        nxt = [[0] * (MAX + 1) for _ in range(MAX + 1)]
        for g in range(MAX + 1):
            for x in range(1, MAX + 1):
                nxt[g][x] = x if g == 0 else gcd(g, x)

        dp = [[0] * (MAX + 1) for _ in range(MAX + 1)]
        dp[0][0] = 1

        for x in nums:
            ndp = [[0] * (MAX + 1) for _ in range(MAX + 1)]

            for g1 in range(MAX + 1):
                row = dp[g1]
                for g2 in range(MAX + 1):
                    cur = row[g2]
                    if cur == 0:
                        continue

                    ndp[g1][g2] = (ndp[g1][g2] + cur) % MOD

                    ng1 = nxt[g1][x]
                    ndp[ng1][g2] = (ndp[ng1][g2] + cur) % MOD

                    ng2 = nxt[g2][x]
                    ndp[g1][ng2] = (ndp[g1][ng2] + cur) % MOD

            dp = ndp

        ans = 0
        for g in range(1, MAX + 1):
            ans = (ans + dp[g][g]) % MOD

        return ans