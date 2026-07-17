
class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        m = max(nums)
        f = [0] * (m + 1)
        for x in nums:
            f[x] += 1

        c = [0] * (m + 1)
        for i in range(1, m + 1):
            for j in range(i, m + 1, i):
                c[i] += f[j]

        g = [0] * (m + 1)
        for i in range(m, 0, -1):
            x = c[i]
            g[i] = x * (x - 1) // 2
            for j in range(i * 2, m + 1, i):
                g[i] -= g[j]

        pre = []
        s = 0
        for i in range(1, m + 1):
            s += g[i]
            pre.append(s)

        return [bisect_right(pre, q) + 1 for q in queries]