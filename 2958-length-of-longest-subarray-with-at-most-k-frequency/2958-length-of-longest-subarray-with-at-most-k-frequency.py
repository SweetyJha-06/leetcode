class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = {}
        left = ans = 0

        for right, x in enumerate(nums):
            freq[x] = freq.get(x, 0) + 1

            while freq[x] > k:
                freq[nums[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans