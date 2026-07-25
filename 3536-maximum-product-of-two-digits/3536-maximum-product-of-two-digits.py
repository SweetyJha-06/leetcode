class Solution:
    def maxProduct(self, n: int) -> int:
        a = sorted(map(int, str(n)))
        return a[-1] * a[-2]