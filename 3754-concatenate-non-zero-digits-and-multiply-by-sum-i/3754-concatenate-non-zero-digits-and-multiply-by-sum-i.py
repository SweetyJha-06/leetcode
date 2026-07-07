class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = s = 0
        for c in str(n):
            if c != '0':
                d = int(c)
                x = x * 10 + d
                s += d
        return x * s