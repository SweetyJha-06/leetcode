class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        a = sorted((v, i) for i, v in enumerate(nums))
        ans = nums[:]
        l = 0

        while l < n:
            r = l
            while r + 1 < n and a[r + 1][0] - a[r][0] <= limit:
                r += 1

            vals = sorted(x[0] for x in a[l:r + 1])
            idx = sorted(x[1] for x in a[l:r + 1])

            for i, v in zip(idx, vals):
                ans[i] = v

            l = r + 1

        return ans