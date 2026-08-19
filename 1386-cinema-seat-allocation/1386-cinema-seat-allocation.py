class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = {}
        for r, s in reservedSeats:
            rows[r] = rows.get(r, 0) | (1 << (s - 1))

        ans = (n - len(rows)) * 2

        for mask in rows.values():
            left = (mask & 30) == 0
            middle = (mask & 120) == 0
            right = (mask & 480) == 0

            if left and right:
                ans += 2
            elif left or middle or right:
                ans += 1

        return ans