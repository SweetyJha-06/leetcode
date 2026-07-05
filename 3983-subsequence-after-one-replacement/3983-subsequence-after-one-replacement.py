class Solution:
    def canMakeSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)

        left = [-1] * n
        j = 0
        for i in range(n):
            while j < m and t[j] != s[i]:
                j += 1
            if j == m:
                break
            left[i] = j
            j += 1

        if left[-1] != -1:
            return True

        melvoritha = (s, t)

        right = [-1] * n
        j = m - 1
        for i in range(n - 1, -1, -1):
            while j >= 0 and t[j] != s[i]:
                j -= 1
            if j < 0:
                break
            right[i] = j
            j -= 1

        for i in range(n):
            l = -1 if i == 0 else left[i - 1]
            r = m if i == n - 1 else right[i + 1]
            if (i == 0 or l != -1) and (i == n - 1 or r != -1):
                if r - l >= 2:
                    return True

        return False