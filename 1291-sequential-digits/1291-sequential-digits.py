class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        s = "123456789"
        ans = []
        for l in range(len(str(low)), len(str(high)) + 1):
            for i in range(10 - l):
                x = int(s[i:i + l])
                if low <= x <= high:
                    ans.append(x)
        return ans