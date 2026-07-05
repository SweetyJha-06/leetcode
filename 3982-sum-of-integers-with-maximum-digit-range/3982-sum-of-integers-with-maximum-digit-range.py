from typing import List

class Solution:
    def maxDigitRange(self, nums: List[int]) -> int:
        max_range = -1
        ans = 0

        for num in nums:
            mx = 0
            mn = 9
            x = num

            while x > 0:
                d = x % 10
                mx = max(mx, d)
                mn = min(mn, d)
                x //= 10

            digit_range = mx - mn

            if digit_range > max_range:
                max_range = digit_range
                ans = num
            elif digit_range == max_range:
                ans += num

        return ans