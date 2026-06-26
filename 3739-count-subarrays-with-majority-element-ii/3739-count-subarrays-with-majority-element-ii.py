from typing import List

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        size = 2 * n + 5
        offset = n + 2

        bit = [0] * (size + 1)

        def update(idx, val):
            while idx <= size:
                bit[idx] += val
                idx += idx & -idx

        def query(idx):
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & -idx
            return s

        prefix = 0
        ans = 0

        update(offset, 1)  # Initial prefix sum = 0

        for x in nums:
            prefix += 1 if x == target else -1
            ans += query(prefix + offset - 1)
            update(prefix + offset, 1)

        return ans