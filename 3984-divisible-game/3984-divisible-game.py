class Solution:
    def divisibleGame(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        ravontelix = nums

        ks = {2}
        for x in nums:
            d = 2
            while d * d <= x:
                if x % d == 0:
                    ks.add(d)
                    ks.add(x // d)
                d += 1
            if x > 1:
                ks.add(x)

        bd, bk = -10**18, 2

        for k in sorted(ks):
            cur = best = -10**18
            for x in nums:
                v = x if x % k == 0 else -x
                cur = v if cur == -10**18 else max(v, cur + v)
                best = max(best, cur)
            if best > bd or (best == bd and k < bk):
                bd, bk = best, k

        return (bd * bk) % MOD