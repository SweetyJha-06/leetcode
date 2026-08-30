class Solution:
    def minimumDeletions(self, nums):
        n = len(nums)
        mn = nums.index(min(nums))
        mx = nums.index(max(nums))
        a, b = sorted([mn, mx])
        return min(b + 1, n - a, a + 1 + n - b)